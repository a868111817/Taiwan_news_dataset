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
    url = r'https://www.epochtimes.com/b5/19/12/27/n11749380.htm'
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
            人心向善的變化,可能就在一念間,我們敏銳地抓住人性善良的瞬間光輝,藉由生命感動生命的
            過程,讓它不斷地擴大...... 一提到監獄,一般人多半直覺想到,這是個什麼樣的地方?多少
            黑幫火拚、毒品走私、刺龍刺鳳......各色大有來歷的角頭老大們聚集於此;又或是高科技
            犯罪、跨國詐欺集團、市井地痞、作奸犯科......各種龍蛇雜處的是非之地。 然而,阿麗
            老師每週排除萬難,驅車百里,與受刑同學一次又一次,點滴互動中,同學逐漸敞開心防,掀開
            內心深處那塊不願揭開的瘡疤...... ~一起看看,阿金的生命故事!~ 「這世上,沒有任何
            歧途不可回頭;沒有任何錯誤不可以改正。」 看著鑰匙圈上的這段話,讓我想起了阿金在上課
            時,跟同學分享互勉的情形...... 阿金說:「老師講了這個故事之後,我就把這段話抄進筆記
            本,時時勉勵自己,『堅持』是很重要的修行。」 故事大意是這樣的: 「山中有座寺廟,一位
            老和尚特別看重一個小和尚,想把他調教成衣缽傳人,奈何小和尚因為不堪修煉的寂寞,有一天
            竟然不告而別,偷偷下山了,從此過著荒唐的歲月! 時光荏苒,一轉眼20年過去了,在一個月光
            皎潔的夜晚,小和尚半夜醒來,看著一片潔白大地,幡然醒悟,他趕回山上,跪在寺廟前三天三夜
            懺悔,請求老和尚的原諒。 老和尚以嫌惡的眼光看著他,指著佛堂的供桌說:『除非佛堂供桌
            開花,我才可能原諒你的。』小和尚最終失望地離去!誰想到!供桌竟然在一夜之間開出燦爛的
            花朵,而且在無風的狀況下搖曳著,好像非常急促地在提醒老和尚,『救人急!』 老和尚恍然
            大悟,趕緊下山尋找小和尚,但是小和尚已經再度墮落風塵!回寺後,老和尚寫下這段話便圓寂
            了。」 阿金說:「這個故事對我來說,太有啟發了!不過,我對故事的情節也有幾點看法。
            」 「沒錯,我們都是犯過錯的人,但是,我們絕對不可以喪志,當我們下定決心要改變自己的
            時候,一定要『堅持』。故事中的小和尚,雖然他起了悔改的念頭,即使跪了三天三夜,但是
            沒有堅持,第四天佛堂的供桌就開花了。如果他的決心夠堅定,整個故事就全都不一樣了!
            」 阿金以大哥的口吻與同學互勉:「我們要牢牢記住,這世上,沒有任何歧途不可回頭;沒有
            任何錯誤不可以改正。」 「討債公司」的大哥大 回想阿金剛進入班級上課的時候,他選擇坐
            在後面,雙手交叉,用銳利的眼神看著老師。 我請他往前坐,他手往天花板一指:「這裡有
            電風扇,比較涼啦!」老師與同學的互動,他也是微笑著冷眼旁觀,很少說話。我想:「又來了
            一位大哥!」 有一次我利用班級間走動的機會,來到阿金旁邊,我問:「請問,你是怎麼進來了
            ?」 阿金:「有位朋友被他的朋友拐騙了好多錢,一直要不回來,最後找到我們公司,請我們
            幫忙。」 我疑惑地問:「竟有這種公司?你們公司是做什麼的?」 一旁的同學阿明解釋:「
            老師,就是幫派啊!只是講『公司』比較好聽啦!」 我說:「幫派!我只聽過竹聯幫。」阿金:
            「是啊!我就是竹聯幫!」 我接著問:「後來,你有要到錢嗎?」阿金答:「原本對方應該償還
            1,600萬元,後來我好好的修理了對方,拿回來1,200萬元。」 我問:「然後呢?」阿金:「
            公司拿到600萬酬謝金。」 我繼續問:「接著呢?」阿金:「因為公司有好多小弟,大家都有
            出力,論功行賞。」 我再問:「那你分得多少?」阿金:「160萬元,結果對方又去告我,所以
            我就進來了。」 當大俠遇到俠女 我驚訝地問:「現在這樣,你覺得值得嗎?」 阿金:「唉呀!
            當時年輕不懂事,怎麼會想這麼多。」 阿金又說:「如果這在古代,我應該是個大俠,其實我是
            行俠仗義,只是現在的法律不允許。」 我答:「照你這麼說,我還覺得自己應該才是俠女呢!」
            阿金:「我看也是!」 我說:「真正的俠客應該是有崇高的道德,還要有一顆仁厚的心,即使
            遇到不公不義的事情,也絕不會輕易動手傷人的。」 阿金側著臉笑著說:「老師,你說的這些
            話,我接受。」 阿金表示,當初會報名參加心靈點滴讀報班,完全只是想找機會給自己透透氣
            ,反正也沒有對課程抱著什麼期望。可是幾堂課聽下來,越來越覺得老師說得很有道理,自己
            也開始反省一路走來的人生路。 反省,一路走來的人生路 原來阿金是個學業成績優良的
            高材生,當年父親希望他有更好的成就,把他送到鄉下擔任校長的叔叔身邊就近教導。 誰知,
            正因為這種特殊的身分,反而給阿金創造機會,結交了各式道上的朋友。因為聰明機伶再加上
            特殊關係保護,好幾次的闖禍也都被和解處理了。在這過程中,阿金加入了幫派,從青少年開始
            ,便數度進出監獄。 幾個月的課程聽下來,阿金靜下心來,好好的反思,以寫回憶錄的方式,
            回顧自己的每個階段,他不再馬虎逃避,而是仔細的審視自己,還勇敢的寫家書,雖然妻子仍然
            不相信他(因為已經一再的被他欺騙、傷害太多次。) 但是,女兒終於回信給他。聰明靈活的
            阿金從信中讀出了家人對他仍抱著一絲希望,他決定這次要真正的改變,不再用過多的言語
            訴說,他要以實際行動讓家人感受到。 阿金,加油!一定要「堅持」,「這世上,沒有任何歧途
            不可回頭;沒有任何錯誤不可以改正。」
            '''
        ),
    )
    assert parsed_news.category == '文化網,人生感悟,心靈陽光,面對逆境'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1577376000
    assert parsed_news.reporter is None
    assert parsed_news.title == '真正的俠義之士'
    assert parsed_news.url_pattern == '19-12-27-11749380'
