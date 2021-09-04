from tqdm import tqdm

import news.crawlers.db
import news.migration.db
from news.crawlers.util.normalize import (company_id, compress_raw_xml,
                                          compress_url)


def v1(
    dataset: news.migration.db.schema.OldNews,
) -> news.crawlers.db.schema.RawNews:
    r'''從舊資料(`OldNews`)中取出raw data需要的部份(`company_id`, `url_pattern`, `raw_xml`)，
    並轉換成正確的格式後保存成`RawNews`
    '''
    result = []
    for i in tqdm(dataset):
        result.append(
            news.crawlers.db.schema.RawNews(
                company_id=company_id(company=i.company),
                url_pattern=compress_url(url=i.url, company=i.company),
                raw_xml=compress_raw_xml(raw_xml=i.raw_xml)
            )
        )
    return result
