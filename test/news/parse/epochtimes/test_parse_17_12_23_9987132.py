import re
import textwrap

import news.crawlers.db.schema
import news.crawlers.util.normalize
import news.crawlers.util.request_url
import news.parse.db.schema
import news.parse.epochtimes


def test_parsing_result() -> None:
    r"""Ensure parsing result consistency."""
    company_id = news.crawlers.util.normalize.get_company_id(company='大紀元')
    url = r'https://www.epochtimes.com/b5/17/12/23/n9987132.htm'
    response = news.crawlers.util.request_url.get(url=url)

    raw_news = news.crawlers.db.schema.RawNews(
        company_id=company_id,
        raw_xml=news.crawlers.util.normalize.compress_raw_xml(
            raw_xml=response.text,
        ),
        url_pattern=news.crawlers.util.normalize.compress_url(
            company_id=company_id,
            url=url,
        )
    )

    parsed_news = news.parse.epochtimes.parser(raw_news=raw_news)

    assert parsed_news.article == re.sub(
        r'\n',
        '',
        textwrap.dedent(
            '''\
            在辭舊迎新之際,新唐人電視台特別企劃《2018跨年繽紛夜》直播特別節目,在2017年的最後
            一個夜晚,12月31日陪伴觀眾盤點年度大事件,歡歡喜喜迎新年。 在全球燦爛煙火、跨年倒數
            計時中,再見2017,哈囉2018!新唐人2018跨年繽紛夜,跨時代也跨國際,讓您耳目
            一新! 先到唐朝吃國際美食,再與韓星一起搬炭送暖,還有神醫孫思邈直播健康1+1;從傳統
            習俗、聖誕節慶台灣、紐約比一比,到走入美食天堂,傳奇時代,1000步的繽紛台灣。 通過
            跨年煙火,跨國接力,在時代廣場一起倒數,迎接2018,新唐人電視台陪伴您許下新年的第一個
            願望。
            '''
        ),
    )
    assert parsed_news.category == '北美新聞,美國華人'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1513958400
    assert parsed_news.reporter is None
    assert parsed_news.title == '2018跨年繽紛夜'
    assert parsed_news.url_pattern == '17-12-23-9987132'
