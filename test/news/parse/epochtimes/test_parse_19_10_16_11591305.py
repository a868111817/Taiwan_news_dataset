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
    url = r'https://www.epochtimes.com/b5/19/10/16/n11591305.htm'
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
            1949年,國權分隔的界線,戰事頻仍,風聲鶴唳。作者王臨冬出身名門後代,卻成為流亡
            學生;用淬礪人生的力量,譜寫半輩子的離散生涯;大時代裡最不堪回首,卻又漾著最具生命力
            的堅忍奮鬥過程。 白天行走時,看著這一座座連綿的山,真不能去想何時才有盡頭,
            一程又一程村莊是沒有個影子,對我們這群來自中原又是八百里平原上的人,真是知透了這個
            地帶的地瘠民貧,也是不毛得人們不能生存。好不容易能見到幾個住戶,土牆、草屋,連家鄉
            人家的牛棚都不如,散亂無章,沒有一點住的文化。令我們更奇怪的是,好不容易發現幾間茅屋
            ,但都是人去屋空,這裡想不會有戰亂,他們更不會是避砲火,可是屋子裡就是沒有一個人,四壁
            更是空無一物,能看到的只是些乾草、朽木、枯枝,他們連個鋪鍋灶的力氣都沒有,如這裡真是
            有人生活的地方,那真是比戰爭洗劫後還要悽慘,這些人究竟到哪裡去了? 一次在一處屋子裡
            發現一種景象,屋子的正中央吊著一根粗繩,繩子向下的盡頭有個大鉤子,鉤子上鉤著一個圓形
            直徑深度各有一尺的鐵鍋,鍋離地有尺餘高,由鍋子裡剩餘著的粒米和焦鍋巴、地上的餘燼和
            被燒得黑焦焦的一塊,可以判斷原來這就是他們的鍋灶,他們就是如此的燒飯。後來每再到
            一處,就會發現一間屋子裡會有一塊焦土和餘燼,但大多數那繩子下吊著的鍋都沒有了,這些
            僅有的居民為何離家他去,一直都令我們不解。 這一處處人去屋空、一無所有的情景,使我們
            這一群夜以繼日奔走的人也無處覓食,軍中弟兄們隨身所帶的食米漸漸用盡,他們也成了自顧
            不暇,一天無足夠的食物自給,更不能和大家分食,飢餓成了大家的問題。但是這後來的日子
            仍要繼續的走,靠著一些奇遇去覓取食物了。 兩天了,沒曾遇到任何食物,難耐的飢餓中萬幸
            遇上了一處山村,飢餓使同學們每個人都不顧一切的在村子裡四處搜尋,一位同學一腳不慎
            踏入了一灘泥沼裡,哪知卻意外的在腳下踩出了一條比手指粗不了多少的番薯,她如獲至寶的
            有意再往下踏,越踏越出奇,裡面全是一條條的小番薯,於是大家一夥兒索性用手抓摸了。原來
            這是居民們的故作的埋藏,這一發現被大家抓出了不少,不少人連忙洗了生嚼,恰巧另外一位
            同學找到了一個破鍋,大家又忙用石頭支起加水來煮番薯,你撿柴他燒火,忙亂中預期這煮熟的
            田薯口水都直往外衝,哪知越燒鍋底就越捲黑煙,原來鍋底有漏水的小洞,於是燒火的人拚命
            煽火,撐鍋的人繼續提水來加,算是勉強把番薯煮成半熟,大家就搶食起來了,誰管有的還
            不乾淨帶有泥土,皮也捨不得除去,狼吞虎嚥吧,這是兩天來第一次飽食,這些小番薯實勝過
            山珍海味。 這天可說是最幸運,不知是誰又在草堆下翻出了些稻穀,一時大家一陣狂喜,但
            如何能食,又是對穀生嘆了,有人就建議用石頭來搗,但何時才能成米?因此又使這位同學計窮,
            又有人說去找碾,荒山僻野這不是家鄉,這意見更是說得離了譜。一位沉思的同學拎起那個
            破鍋說:「我們用這個來炒嘛!」於是大家不約而同的都像開了竅,拿著穀子就往這個破鍋裡倒
            ,鍋底一加熱,這些穀子即開始啪的不停開出白花,一粒粒穀子都變大起來了,大家樂得臉上像
            穀花一樣的裂開歡喜的笑。更雀躍撿拾蹦出鍋的米花來吃,感覺味道更是無比的焦香,於是這
            粒粒炸出的穀花,大家更視如珍珠般的可貴了,邊炒邊想辦法去儲存,不少人脫下一件上衣,
            把袖口紮起來,用兩條袖子做口袋,把穀花裝得滿滿的,於是大家都有了存量,這是上天特別的
            支助吧?由於這個大發現,隊伍在這裡停得最久,軍中的弟兄們也都如法炮製,人人都是滿載。
            往後的幾日就是遇不上一處村鎮,沒有人煙的地方,食物難找猶如上青天,大家就這樣一把一把
            咀嚼這所積存的穀花,遇上山泉就狂飲一陣,在這段行程中,生命就是這樣苟延了。 肚子餓了,
            只有這粒粒的穀花暫時的維繫一下,山路的坡度越來越高,氣喘得像要把嘴裡的舌頭都要吞下
            肚去,胸部喘得收縮發痛,不少人邊喘邊擠出那一聲聲我不走了!我不能走了的語句,但是口中
            在說,腳可是並不敢停下,兩邊的山高得也像是要擠攏過來,隊伍仍是做一字行,就在這時,兩邊
            的山腰間突然響起了稀疏的槍聲,有時像是對空射擊,響聲落入谷底就像是陰天的一串炸雷,
            有時平射在山間,激起些回聲像是槍從四面射來,驚得人不住的打顫,雖飢餓疲累,喘得接不
            上氣,然更得加快腳步。這槍聲是個大的震撼,軍中的弟兄們都急持槍做準備還擊狀,氣氛就
            更緊張了,但他們只做戒備,並沒有向任何一方槍響處還擊,山路是如此的陌生、艱險,如在此
            遭到圍攻,看只有損兵折將百無生路了,也許這就是他們只做戒備,而不做任何還擊的原因吧,
            我們這一群赤手空拳的學生,想也是他們不便在此槍戰的原因!槍聲仍是不斷,偶爾啾的一聲,
            會有一顆流彈,情況漸次更可怖了,軍中的長官們下達命令,要這列本就單行的隊伍,人與人
            之間快再拉長距離,以減少流彈的命中機會。 命令一道道的往後傳來,飢餓、疲累、喘氣,
            又加上死亡的恐懼,這是人類求生本能的一股特有的力量吧,每人都更快更快的加緊腳步。把
            人與人之間的距離也加長了再加長,槍聲不斷的在響,時而也有流彈在頭頂穿過,這顯見的是
            山頭躲藏的持槍者,是向這支隊伍挑釁,部隊一直保持著鎮定,傳令讓大家肅靜急走,趕快衝出
            危險區。這隨時都會被流彈射殺的恐懼,我覺得全身的汗毛一直都豎立著。 又一陣的狂射,
            落地的子彈好像多起來了,遠遠在前面的一截隊伍有點亂了的騷動,一會兒傳下來一位叫
            杜達先的同學被流彈射中了,據傳是子彈自大腿處又穿入下小腹,漸漸的路上有他片片的血跡,
            也頻傳著他疼痛的哀號,悽慘更震人心腹,不少的同學因驚恐而流淚了,大家都也不住探聽
            杜同學的情況,這都是得靠著一個人一個人慢慢的傳達,最後說衛生連的弟兄們給他包紮後,
            用擔架把他抬起來了。這件意外的事發生後,前面要大家加長距離的傳令就更頻仍了,長官們
            也一再傳令安慰大家,今晚一定能到達一個鎮市,讓大家多忍耐,盡力能快點走。
            '''
        ),
    )
    assert parsed_news.category == '生活,生活萬象'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1571155200
    assert parsed_news.reporter is None
    assert parsed_news.title == '回首流亡路:1949外一章'
    assert parsed_news.url_pattern == '19-10-16-11591305'
