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
    url = r'https://www.epochtimes.com/b5/19/12/24/n11743216.htm'
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
            法國的奧塞美術館裡,收藏著畫家米勒的一幅著名的油畫《拾穗者》。它創作於1857年,以
            《聖經》故事為藍本,描繪了三位農婦在金黃色的麥田中拾穗的情景。整幅畫筆法簡潔生動
            ,色調明快柔和,刻畫出當時的社會狀況。不過朋友們,您知道嗎,在唐詩中,也有一首詩描繪
            了一位拾麥穗的婦人,不過她的生活,比那三位農婦艱辛多了。 故事發生在一千多年前的一個
            酷暑。在北方的麥田裡,有許多農夫在辛勤地收割麥子。他們的腳底熏蒸著地面的熱氣,後背
            烤著火辣的陽光,哪怕很累了都不肯休息片刻。這時,一位抱著孩子的農婦,也來到這片忙碌
            的土地,右手拿著零散的麥穗,左臂挎著一個破筐——原來她在撿地裡遺落的麥穗。她告訴周圍
            的人,因為賦稅繁重,家裡的田地都賣掉了,現在只能撿些麥穗充飢。 這時,有一位官員路過
            聽到了她的遭遇,有感而發寫下一首詩歌,記錄下老百姓的現實生活。他就是中唐著名的現實
            主義詩人白居易,這首詩就是他的代表作之一《觀刈麥》: 「田家少閒月,五月人倍忙。夜來
            南風起,小麥覆隴黃。 婦姑荷簞食,童稚攜壺漿,相隨餉田去,丁壯在南岡。 足蒸暑土氣,
            背灼炎天光,力盡不知熱,但惜夏日長。 復有貧婦人,抱子在其旁,右手秉遺穗,左臂懸敝筐
            。 聽其相顧言,聞者為悲傷。家田輸稅盡,拾此充飢腸。 今我何功德,曾不事農桑。吏祿三百
            石,歲晏有餘糧。 念此私自愧,盡日不能忘。」 詩境賞析 《觀刈麥》,刈是收割的意思,這首
            詩描寫的是詩人在田邊看到農民收割夏麥的所思所感。這是一首敘事詩,層次非常分明,反映
            當時的社會狀況以及農民生活的艱難。這首詩可以分為四個部分。第一部分是詩歌的前四句,
            交待了故事發生的背景。「田家少閒月,五月人倍忙」,農戶一年到頭都沒有閒暇的時候,到了
            黃曆的五月就加倍繁忙。詩人接下來說明原因:「夜來南風起,小麥覆隴黃。」原來,夏季到了
            ,小麥大片成熟,而北方的夏天又是多雨的季節,所以一定要趕快收割麥子,這一年才能有好的
            收成。 第二部分就是後面八句,描寫農家男女老小參與刈麥的情景。「婦姑荷簞食,童稚攜壺
            漿」,體力較弱的婦孺,主要負責後勤方面的工作。家裡的媳婦們無論長幼,都用竹筐挑著
            食物,小孩子也提著壺裝的湯湯水水,早早從家裡出發了。「相隨餉田去,丁壯在南岡。」
            婦孺們一路往南山岡走去,原來是為在那裡勞作的男人們送飯食。 那麼男人們在做什麼呢?
            「足蒸暑土氣,背灼炎天光,力盡不知熱,但惜夏日長。」他們面朝黃土背朝天,正在炎炎夏日
            裡收割麥子。他們踩在灼熱的土地上,腳下蒸著暑氣;頭頂似火的驕陽,整個身體都被烈日暴曬
            著。做體力活本就是一件辛苦的事,何況遇到這酷熱的天氣?很快他們就精疲力盡了,但是每個
            人都像不知道熱一樣,繼續低頭勞作,因為夏日時間長,可以讓他們有更多的時間來完成農活呀
            。 「力盡不知熱,但惜夏日長。」《唐宋詩醇》評價這兩句「曲盡農家苦心」,它通過農民
            反常的心理,傳神地表現出百姓生活的辛酸。誰都知道夏天幹活辛苦,但是他們偏偏珍惜這
            漫長的白天時光,好讓他們有更多的時間完成工作。這種寫法,是不是和詩人另一首《賣炭翁》
            裡的「可憐身上衣正單,心憂炭賤願天寒」,有異曲同工之妙呢? 接下來八句,一位貧苦的農婦
            出場了。「復有貧婦人,抱子在其旁。」她懷裡抱著孩子,說明家裡可能無人幫她照看幼子,
            或許是個孤苦伶仃的寡婦。「右手秉遺穗,左臂懸敝筐。」這位農婦是無法收割麥子的,只能
            在田地裡尋找一些遺落的麥穗。「聽其相顧言,聞者為悲傷。家田輸稅盡,拾此充飢腸。」婦人
            向周圍人講述自己的身世,因為家裡不堪賦稅的壓力,把田產都變賣了,這時候只能拾些麥穗來
            充飢。 聽到這番話的人,無不感到憂傷。為什麼呢?他們都是鄉鄰,沉重的賦稅壓得每個人都
            透不過氣來。今年的拾穗者也許就是去年的刈麥者,而今年尚能刈麥的人,明年是否還有田地
            供他們去揮汗勞作,維持家計?他們的傷心,既是對貧婦的同情,也是對未來命運的憂愁。 最後
            幾句就是詩歌的第四部分了。詩人耳聞目睹了這一切,憂國憂民的情懷湧上心頭。「今我何
            功德,曾不事農桑。吏祿三百石,歲晏有餘糧。」他感嘆有幸走上讀書入仕這條路,不必從事
            農桑。而且他雖然是個小官,卻能不用勞作就享有每年三百石的俸祿,年底還有剩餘的糧食。「
            念此私自愧,盡日不能忘。」詩人身為父母官,不忍見百姓深受賦稅之苦,因而感到難過而慚愧
            ,這種憂悶的情緒久久縈繞心頭,不能釋懷。 詩人背後的故事 談到詩人白居易,大家往往津津
            樂道於他的兩首長詩《琵琶行》和《長恨歌》,那優美的文字、細膩的情感千百年後仍然能
            打動人心。但是您知道嗎,在白居易心中最看重的卻不是這兩首詩。他在《與元九書》中,把
            自己的作品分成四類,第一是諷喻詩,表達其兼濟天下之志;第二是閒適詩,表達其獨善其身之
            志;之後是有感而發的傷感詩和其它的雜律詩,他認為這兩類都屬於抒情、應酬之作,「非平生
            所尚者」。 《觀刈麥》沒有華麗的辭藻,也沒有浪漫的故事,卻是白居易最推崇的那一類諷喻
            詩。在唐憲宗元和初年,白居易在陝西任縣尉,主管緝捕盜賊、徵收賦稅等事務。當看到當地
            百姓生活如此困窘時,白居易便寫下這首反映民間疾苦的《觀刈麥》。 夏天到了,白居易不去
            描寫陰陰夏木、映日荷花這樣的美景,卻把目光投注到田地上辛勤勞作的農人,為社稷、為百姓
            寫下平易樸實、又字字千鈞的詩歌。這是為什麼呢?這源於白居易作詩的一貫主張,他和詩人
            元稹都是「新樂府運動」的倡導者。樂府詩以兩漢為代表,因具有「感於哀樂,緣事而作」的
            諷喻時政的精神,從漢武帝起,朝廷開始收集民間樂府詩,了解風土民情、地方政務。 到了
            唐朝,白居易等人主張恢復古時候的采詩制度,讓詩歌再次起到補察時政的作用。他提出「文章
            合為時而著,歌詩合為事而作」的詩歌理論,本人也用樂府新題創作許多諷喻詩,並把自己創作
            的新樂府編成集子,還在序言中提出新樂府詩歌的創作原則,即文辭質樸,切中時弊,作詩要為
            君、為民、為物、為事而作,不為文而作。因而白居易的許多詩作,都對國家弊政、社會問題
            提出委婉的批評,也就是「唯歌生民病,願得天子知」。 其實,白居易不僅是一位有責任感的
            詩人,也是盡忠職守的官員。他主要生活在唐憲宗時代,憲宗是盛唐之後很有作為的皇帝,曾
            大力征討藩鎮,讓唐朝再次出現統一的中興局面,史稱「元和中興」。 白居易在三十多歲時入
            朝為官,創作的諷喻詩在士人君子之間廣泛流傳,甚至傳到宮廷,也受到憲宗的賞識。因此,他
            被拜為翰林學士,又擔任左拾遺、也就是一種言官。為報答憲宗的知遇之恩,白居易多次懷著
            拳拳忠心上書言事,也繼續創作大量的諷喻詩,讓詩歌能成為皇帝考察執政得失的一面鏡子。
            白居易的一片忠誠也得到皇帝的敬重,去世後被追贈尚書右僕射,謚號「文」。繼位的唐宣宗
            親自作詩,說道「文章已滿行人耳,一度思卿一愴然」,表達了對一代忠臣的深沉悼念。 白居
            易一生中,既有《觀刈麥》這樣的諷喻詩,也有《琵琶行》這樣的抒情敘事詩,那麼您更喜歡哪
            一種呢?或許這很難選擇,但這些詩作卻讓我們了解到,白居易不僅是一位才華橫溢的文人,更
            是一位心懷天下的君子。
            '''
        ),
    )
    assert parsed_news.category == '文化網,文學世界,文學賞析,唐詩'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1577116800
    assert parsed_news.reporter is None
    assert parsed_news.title == '唐詩裡的拾穗者'
    assert parsed_news.url_pattern == '19-12-24-11743216'
