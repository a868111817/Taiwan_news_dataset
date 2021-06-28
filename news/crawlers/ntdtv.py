import re
from collections import Counter
from datetime import datetime
from typing import List

import dateutil
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

import news.crawlers
import news.preprocess
from news.db.schema import News

FIRST_PAGE = 1
URL_PATTERN = re.compile(
    r'https://www.ntdtv.com/b5/(\d+)/(\d+)/(\d+)/a\d+.html'
)


def get_news_list(
    category: str,
    current_datetime: datetime,
    api: str,
    past_datetime: datetime,
    *,
    debug: bool = False,
) -> List[News]:
    news_list: List[News] = []
    logger = Counter()

    # Get max page of this category.
    try:
        url = f'https://www.ntdtv.com/b5/prog{api}/1'
        response = requests.get(
            url,
            timeout=news.crawlers.util.REQUEST_TIMEOUT,
        )
        response.close()

        # Raise exception if status code is not 200.
        news.crawlers.util.check_status_code(
            company='ntdtv',
            response=response
        )

        soup = BeautifulSoup(response.text, 'html.parser')
        max_page = soup.select('div.pagination > a.page-numbers')[-2].text
        max_page = int(max_page.replace(',', ''))
    except Exception as err:
        if err.args:
            logger.update([err.args[0]])

        # Only show error stats in debug mode.
        if debug:
            for k, v in logger.items():
                print(f'{k}: {v}')
        return []

    # Only show progress bar in debug mode.
    iter_range = range(FIRST_PAGE, max_page)
    if debug:
        iter_range = tqdm(iter_range, desc='Find start page loop')

    # Find start page loop.
    start_page = 1
    for page in iter_range:
        page_url = f'https://www.ntdtv.com/b5/prog{api}/{page}'

        try:
            response = requests.get(
                page_url,
                timeout=news.crawlers.util.REQUEST_TIMEOUT,
            )
            response.close()

            # Raise exception if status code is not 200.
            news.crawlers.util.check_status_code(
                company='ntdtv',
                response=response
            )

            # Parse date in this page.
            soup = BeautifulSoup(response.text, 'html.parser')
            a_tags = soup.select(
                'div.post_list > div.list_wrapper > div.one_post div.title > a'
            )
            matches = filter(
                bool,
                map(lambda a_tag: URL_PATTERN.match(a_tag['href']), a_tags)
            )
            news_datetimes = map(
                lambda match: {
                    'year': int(match.group(1)),
                    'month': int(match.group(2)),
                    'day': int(match.group(3)),
                },
                matches,
            )
            news_datetimes = list(map(
                lambda n: dateutil.parser.isoparse(
                    f"{n['year']:04d}-{n['month']:02d}-{n['day']:02d}T00:00:00Z"
                ),
                news_datetimes,
            ))

            # Break loop if `news_datetime < past_datetime`.
            if news_datetimes[0] < past_datetime:
                break
            # If this page contains valid news, we start crawling from this page.
            news_datetimes = filter(bool, map(
                lambda n: past_datetime <= n <= current_datetime,
                news_datetimes,
            ))

            news_datatimes = list(news_datetimes)

            if news_datetimes:
                start_page = page
                break
        except Exception as err:
            if err.args:
                logger.update([err.args[0]])

    # Only show progress bar in debug mode.
    iter_range = range(start_page, max_page)
    if debug:
        iter_range = tqdm(iter_range, desc='Crawling loop.')

    # Crawling loop.
    is_datetime_valid = True
    for page in iter_range:
        if not is_datetime_valid:
            break

        page_url = f'https://www.ntdtv.com/b5/prog{api}/{page}'

        try:
            response = requests.get(
                page_url,
                timeout=news.crawlers.util.REQUEST_TIMEOUT,
            )
            response.close()

            # Raise exception if status code is not 200.
            news.crawlers.util.check_status_code(
                company='ntdtv',
                response=response
            )

            # If `status_code == 200`, parse links in this page.
            soup = BeautifulSoup(response.text, 'html.parser')
            a_tags = soup.select(
                'div.post_list > div.list_wrapper > div.one_post div.title > a'
            )
        except Exception as err:
            if err.args:
                logger.update([err.args[0]])
            continue

        for a_tag in a_tags:
            try:
                news_url = a_tag['href']

                response = requests.get(
                    news_url,
                    timeout=news.crawlers.util.REQUEST_TIMEOUT,
                )
                response.close()

                # Raise exception if status code is not 200.
                news.crawlers.util.check_status_code(
                    company='ntdtv',
                    response=response
                )

                # Parse news in this page.
                parsed_news = news.preprocess.ntdtv.parse(ori_news=News(
                    raw_xml=response.text,
                    url=news_url,
                ))
                news_datetime = dateutil.parser.isoparse(parsed_news.datetime)

                # If `news_datetime > current_datetime` just continue.
                if news_datetime > current_datetime:
                    continue
                # If `past_datetime > news_datetime` stop crawler next news.
                if past_datetime > news_datetime:
                    is_datetime_valid = False
                    break

                news_list.append(parsed_news)
            except Exception as err:
                if err.args:
                    logger.update([err.args[0]])

    # Only show error stats in debug mode.
    if debug:
        for k, v in logger.items():
            print(f'{k}: {v}')

    return news_list


CATEGORIES = {
    '國際': 202,
    '港澳': 205,
    '財經': 208,
    '健康': 1255,
    '體育': 211,
    '美國': 203,
    '大陸': 204,
    '文史': 647,
}


def main(
    current_datetime: datetime,
    db_name: str,
    past_datetime: datetime,
    *,
    debug: bool = False,
):

    if past_datetime > current_datetime:
        raise ValueError('Must have `past_datetime <= current_datetime`.')

    # Get database connection.
    conn = news.db.util.get_conn(db_name=db_name)
    cur = conn.cursor()
    news.db.create.create_table(cur=cur)

    for category, api in CATEGORIES.items():
        news.db.write.write_new_records(
            cur=cur,
            news_list=get_news_list(
                category=category,
                current_datetime=current_datetime,
                debug=debug,
                api=api,
                past_datetime=past_datetime,
            ),
        )

        conn.commit()

    # Close database connection.
    conn.close()
