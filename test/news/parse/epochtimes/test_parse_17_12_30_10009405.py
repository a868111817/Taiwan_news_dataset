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
    url = r'https://www.epochtimes.com/b5/17/12/30/n10009405.htm'
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
            中國民間有句話,叫「閱透人情知紙厚」,意思是說
            人情很薄,薄到還不如紙的厚度。當然,因為人的這個「情」是最不穩定的東西,說變就變,
            甚至說翻臉就翻臉。 估計曾經紅極一時的小燕子趙薇,現在對人情冷暖應該有比較深的體會
            。前兩天她在美國社交媒體上發布了一張近臉照片,並且附上了一句話:看盡人生百態。短短
            的一句話,當然是趙薇最近一個階段心情的反應,也就是發生的一系列的事,讓她看到了世態炎
            涼。 但是奇怪的是,現在趙薇的「看盡人生百態」這個留言,已經不見了,我想美國的社交
            媒體不會也有刪帖的現象吧?如果不是被刪帖,那趙薇發了帖子之後,為什麼又要拿下來呢?是
            受到了什麼壓力嗎?還是自己覺得這樣會得罪人、不太妥當呢?帖子裡也沒有點名道姓啊?
            不知道什麼原因,反正這個留言已經不見了。 但是,有中共背景的海外媒體對這件事忙著熱炒
            ,並直言趙薇的「看盡人生百態」可能是在影射之前的朋友,同時大陸多家媒體紛紛轉載。另外
            還有一件事,中共官媒新華社又點名趙薇,說她是2017A股最富戲劇性的人物之一,讓我們感覺
            趙薇似乎又在被中共敲打了。 這篇文章說趙薇曾經被稱為「女版巴菲特」,完成重慶
            路橋、唐德影視和阿里影業的投資,尤其是後面兩個,趙薇的斬獲頗豐。另外文中也提到了
            趙薇準備計劃用30.6億元人民幣的價格,收購萬家文化。而趙薇自己僅僅出資6000萬元,借款
            約15億元,此外她還拿沒有到手的萬家文化股票質押融資,又獲得了15億元,玩轉51倍槓桿
            。 不過這筆交易最終是以失敗告終了,而且趙薇還遭到了證監會的處罰。證監會認為,趙薇的
            行為對市場秩序有著嚴重影響,損害了中小投資者的信心,影響市場的公平、公正、公開
            。證監會對黃有龍、趙薇、趙政給予警告,並分別處以30萬元罰款;黃有龍、趙薇分別被禁止
            5年內不能進入證券市場。趙政是趙薇的哥哥,黃有龍是趙薇的丈夫。 這個黃有龍有一點神祕
            ,他的發跡、起家都令人匪夷所思。根據公開的資料顯示,黃有龍最初就是一個名不見經傳的
            草根一族,但是在深圳中航康藝娛樂公司待了兩年之後,年僅25歲的黃有龍在2001年買了
            一套234萬元的商品房,另外還辦起了公司。更讓人想不到的,據中國經營網《等深線》的
            深入調查,發現黃有龍一個人在香港還註冊了27家公司。 大陸新媒體「明天財訊」調查發現
            ,有越來越多的線索顯示,黃有龍可能與「明天系」有著一定的聯繫,換句話說,他可能是
            「明天系」的一個棋子。我們知道「明天系」的實際控制人肖建華已經被中共抓了,今年1月
            27號,肖建華從香港被帶回了北京,之後趙薇夫婦就麻煩不斷。
            '''
        ),
    )
    assert parsed_news.category == '新聞看點'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1514563200
    assert parsed_news.reporter is None
    assert parsed_news.title == '趙薇「看盡人生百態」帖子被刪'
    assert parsed_news.url_pattern == '17-12-30-10009405'