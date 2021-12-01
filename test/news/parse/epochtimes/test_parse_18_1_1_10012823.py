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
    url = r'https://www.epochtimes.com/b5/18/1/1/n10012823.htm'
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
            永別中共,徹底決裂邪靈! 從小喜歡學習歷史地理政治等文科知識,經過多年的積澱,自我感覺
            積累甚厚,沒想到的是,半生興趣竟然是一紙謊言,多年來,一心向善,卻終不得果! 從來沒有
            意識到是被邪靈毒害,事實上,我的家人至今受到它刻骨的殺戮而至今仍不覺醒! 短短的十個月
            時間,我終於明白生命的可貴,人生過往的浪費,所有很多之前解不掉的心結終於找到了答案,
            為什麼真心,真話,真相一直不被人接受,為什麼在這個邪魔地獄一直舉步維艱!終於找到答案
            ! 從2017年最後一天聲明,退出所有加入過的邪靈團隊,團隊,劃清界限!讓邪靈盡速退出中華
            神地,還我們所有人純潔美好的人生! 聲明人: 木子水壽 2017-12-31 21:28 退黨
            聲明 本人是一名醫生,也是一家醫院的負責人,因藥商從我單位進了一點管制藥品,本人也被
            牽涉到一件刑事案件中。在同浙江某市公安局、檢察院和法院打交道的過程中,我清清楚楚的
            看到了中共「公檢法」的黑暗腐敗和邪惡,誘供、栽贓、亂扣罪名、變著法的敲詐當事人的
            錢財。如果不是親身經歷,我真的不敢相信共產黨的「公檢法」原來是這麼樣的黑。 現在,
            我接受大法弟子的善言相勸,順應滾滾退黨大潮,同意聲明退出共產邪黨的一切組織,抹去共產
            邪靈打在身上的邪惡獸印,不與邪黨為伍,支持法輪功,在天滅中共的時侯免遭淘汰,保平安
            。 特此聲明。 聲明人: 姜醫生 2017-12-31 21:57 湖北省武漢市 聲明 我是來北京做
            小本生意的外地人,爭些錢以養家糊口!現被作為低端人口只得回家!我現活得很累!我只有退出
            中共才會感到生活得輕鬆、自在、平安!並有一個美好的未來! 聲明人:平安 2017-12-
            31 22:05 中國大陸 退黨退團退隊 我是專門給黨政機關的頭頭們開車,大陸新聞關於法輪功
            的報導都是記者為了完成政治任務而造的假,並且共產黨作惡多端,那些領導們也是當面一套,
            背後一套。知道了天滅中共的預言,我鄭重聲明退出曾經加入過的中國共產黨、共青團、少
            先隊。 聲明人: 李幸運 2017-12-31 23:56 中國黃山
            '''
        ),
    )
    assert parsed_news.category == '大陸新聞,社會萬象'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1514736000
    assert parsed_news.reporter is None
    assert parsed_news.title == '每日三退聲明精選'
    assert parsed_news.url_pattern == '18-1-1-10012823'