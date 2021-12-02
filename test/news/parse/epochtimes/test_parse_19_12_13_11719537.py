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
    url = r'https://www.epochtimes.com/b5/19/12/13/n11719537.htm'
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
            美國對中國股票的投資約為1.9兆美元,並在中國債券上有另外一兆。這些數字基本等於中國
            外匯儲備的規模,並可以輕鬆支付中國的一帶一路計劃。然而,這些中國公司中的一大部分造成
            了國家安全方面的擔憂,參與了侵犯人權並涉及欺詐行為。這對美國意味著什麼?其帶來的影響
            有多大?如果對此不聞不問會帶來什麼後果? 請看我對羅傑‧羅伯遜(Roger Robinson)的
            採訪。羅傑在里根時期擔任國安委國際經濟事務高級總監,后在國會美中經濟與安全評估
            委員會任職,他是揭露這一黑幕問題的人。 貿易戰不是主戰場 羅傑‧羅伯遜:貿易是美中關係
            中一個搶眼的問題。他們(中共)能應付貿易戰之類的問題嗎?是的,這對他們有些痛苦,但是,
            他們能,他們能一直玩下去。看看那些事情起落吧。你知道的,你沒有看到他們有任何驚慌
            失措。他們只是把貨幣貶值或者做些其它事情來抵消關稅的負面影響。 他們也認為,我們的
            農民和其它受害的經濟部門會對川普施壓,起到掣肘的作用。換句話說,他們把這些事情玩到
            了很深的程度。當我們來到高技術領域時,他們就不那麼喜歡了。那可不是這麼舒服的。他們
            不希望我們從保護國家安全和人權的角度出發,去調查海康威視、中興、華為和其它企業
            。 但是他們能忍受那種局面,因為對中興的制裁有條件地解除了,他們也在計劃讓華為免於
            制裁。他們甚至在努力把「曠視科技」從實體名單上拿掉⋯⋯人工智能。也就是說他們可以
            辦得到。 我來告訴你他們最怕的是什麼⋯⋯缺錢,被趕出美國資本市場。因為能否繼續從美國
            資本市場融資關係到中共政權的存亡。 第一部分:節儉儲蓄計劃的決策 旁白:2019年11月
            18日,節儉儲蓄計劃(TSP)董事會再次確認了2017年的決定:從2020年某個時間開始追蹤
            MSCI全球非美國投資市場指數。這一決定使得它的國際基金不僅可以投資發達國家,如西歐
            和北美國家,也能投資新興市場國家中那些正在增長的經濟體,如中國。 TSP董事會受到了
            來自兩黨參議員的壓力,參議員馬可‧盧比奧曾兩次寫信給董事會敦促他們改變決定,因為中國
            公司不符合透明標準並且他們的很多操作違背美國利益。 TSP董事會之後發布了一個聲明,
            稱他們的決定對計劃參與者和受益人最為有利,是投資領域當前的最佳做法,並在當今市場上
            被廣泛認為是聰明的策略。 蕭茗:非常感謝羅伯遜先生今天接受我們的採訪。 羅傑‧羅伯遜:
            我很高興。 蕭茗:TSP董事會堅持他們的立場,他們說十家最大的美國公司的401(K)計劃都
            投資新興市場,就像十家最大的聯邦承包商計劃和六家最大的博時基金供應商那樣,還有其它
            很多。因此他們也有權做同樣的事情。你怎麼看待這件事情? 羅傑‧羅伯遜:嗯,我看了那封信,
            他們也用了像這樣的措辭:「謹慎地採取這一步驟,正確的,對會員最有利的」⋯⋯整個文本你
            都看到這些。實際上他們用了全球非美國(投資市場)指數的增長以及其廣泛使用為他們這樣
            做辯解。事實是過去20年在美國資本市場上沒有篩選機制。 沒有人在意和盡職調查國家安全
            或者與人權有關的問題。結果是北京感到實際上有機可乘。他們覺得資本市場沒有監管,他們
            不被任何人在意。在今年三月之前他們從未出現在國會或者行政分支甚或媒體的議題中。
            你甚至在非政府組織社區也找不到任何評論。也就是說美國對中國在資本市場上的所為視而
            不見。 從美國投資者手裡 北京拿走3兆美元 結果是:北京看到了機會,他們不僅積極把他們
            的股票、債券帶進來,到目前為止從美國機構和個人投資者手裡拿走3兆美元,而且這個數字
            可能還會極大地增加。而他們(TSP)對使用哪個條款,把什麼樣的公司送進美國市場不是特別
            謹慎。 那些在外資管理辦公室制裁名單或者實體名單上,也就是商務部的所謂「黑名單」上
            的公司,例如,先進武器製造商,以及那些對惡劣人權侵害負有責任或者起推手作用的公司,
            如製造監控攝像頭的公司,在關押上百萬維吾爾人的集中營的高墻上每隔幾米就有一個這種
            攝像頭。 這當然是指如海康威視這樣的公司,和中興公司一樣,它也在MSCI全球非美國投資
            市場指數中,還有如中國航空工業集團這類先進武器製造商,它製造噴氣發動機和瞄準美國
            城市的洲際彈道導彈。換句話説,在今天的美國資本市場上我們有很多來自中國的壞演員。
            這些代表了對美國投資者的風險。 我們允許中共軍隊的公司或者與嚴重人權侵害有關的公司
            進入我們的市場,這十分令人震驚,但是不止這些,放下這個不説,我們首先看到這些公司是被
            制裁的。結果是,他們(TSP)造成了對那些中國公司的股價和聲譽的風險,也給冒險投資他們
            的美國投資者造成風險。這怎麼能代表570萬聯邦雇員的最大利益?投資中共軍隊和集中營
            怎麼能服務於聯邦雇員的最大利益?要知道他們中很多人的整個職業生涯都在對抗這類組織
            。 所以你可以看到如我所説,節儉儲蓄計劃董事會視野狹窄,他們官方正式一點的名稱叫聯邦
            退休節儉投資董事會。他們看投資回報,看到所有人都這麼做,他們看他們的信託責任,而這
            其實非常狹隘。那麼,有重大風險怎麼辦?那是個市場條件,那不是來自外部的抱怨,如對社會
            負責的投資會面對和考慮的那樣。也就是說他們有意要忽略這類事情。我認為在做這個決定
            時他們漏掉了根本的東西。這是個基於錯誤判斷的決定,我不認為它站得住腳。 蕭茗:好的。
            因此,我有兩個問題。第一,從美國政府的角度來看,這不應該發生,對吧?這些在制裁名單上
            的公司,經常在制裁名單上,甚至在實體清單上的公司,怎麼能將它們包含在MSCI指數中?這個
            體制出了什麼問題?(只是因為)我們沒有監管機制還是什麼? 羅傑‧羅伯遜:好吧,這是對的。
            我們對這個問題熟視無睹了20年。美國證券交易委員會(SEC)不認為制裁會對這些中國公司
            的股票價值、聲譽造成影響,以及可能對美國投資者構成重大風險。你可以看到這在邏輯上
            講不通。因此,這當然是步調不一,確實是明顯的步調不一。 如果法律不允許你與這些特定的
            公司開展業務,但你可以投資它們,可以為其提供資金,可以給予它們信譽,成為世界上最有
            深度、最龐大的市場中的一員,你知道他們將其用作「質量認可證」,在全球合理化自己的地位。
            進入美國資本市場是一種特權。這不是與生俱來的權利。這一點被混淆了。 中國公司不遵守
            聯邦證券法 羅傑・羅伯遜:中國人和華爾街認為這是對的。不是。您必須遵守規則。中國
            公司不遵守聯邦證券法。它們並沒有像每個美國公司一樣需要接受美國上市公司會計監督
            委員會(PCAOB)審核。它們不遵守多德-弗蘭克(Dodd-Frank)法規和薩班斯-奧克斯利
            (Sarbanes-Oxley)法規。你知道他們不披露財務信息,因為它們被視為國家機密。這可真
            便利。我希望我可以對我的銀行說,(當他們說)「好吧,你知道的,在給你房屋貸款前我想先
            查看下您的財務狀況」。 我說:「很抱歉,但是那是特權信息。你知道,我不會給你這些信息
            」。銀行會很快告訴我,「再見」。這也是我們應該做的。因此,中國擁有美國公司所沒有的
            特權待遇。我倒是希望有人能告訴我這不是事實。但這就是事實。因此,我們處於這種極不
            平衡的局面。你不必擔心聯邦證券法,你不必擔心重大風險,當涉及到威脅國家安全和侵犯
            人權問題時,儘管這些是可制裁行為,並且經常有公司會因此而被制裁。然而,當一家中國公司
            受到制裁時,今天我們的態度是:「即使如此,這筆投資的回報率還不錯吧?」 蕭茗:即使在
            獲得良好的投資回報這點上,......你知道,那些中國公司,幾乎所有的,都擁有兩到三套會計
            記錄,一套用於內部使用,一套提供給稅務局,而且,如果一家公司試圖進行首次公開募股,那麼
            它有第三套可供首次公開募股使用。因此,你怎麼能相信這些公司記錄(如果你是個機構
            投資者),當投資者說他們只看財務收益時,難道不認為這對他們的(投資者)構成財務風險嗎
            ? 羅傑‧羅伯遜:他們基本上都裝作視而不見。他們看到了中國3萬億美元的外匯儲備,儘管
            他們可能不會公開說出來,但他們基本上指望的是,如果這些公司搞欺詐,中國政府會負起責任。
            比方說以前的嘉漢林業,這是個過去非常有名的案例,實際他們沒有森林。換句話說,數十億
            美元的欺詐並不罕見。 你知道,中國大陸的交易所,任何人都會告訴你這是無法無天的西部。
            你是在一個賭場,而不是在一個建立良好、根基穩固、堅實的市場。當你在中國的交易所裡時,
            你就是在流沙中。然而,我們的股指提供商很樂意一次收購數百家公司。你知道,據報導,富時
            羅素指數,他們在今年6月去了中國,他們在一個月內把1097家中國公司列入他們的樣本股
            。 羅傑‧羅伯遜:他們做了多少努力?他們有沒有調查這些公司的子公司?他們看過實體清單或
            制裁清單嗎?他們有沒有去證實到底他們是先進武器製造商還是人權踐踏者?當然沒有。他們
            認為那是別人的工作。這是交易所交易基金發起人的工作,這是資產經理的工作,他們將建立
            一個基金,一個可投資的基金,圍繞這個指數列表。 他們會說,「我們只提供公司名錄」。
            我們想要一個包羅萬象的公司名錄,代表所有不同的經濟實體和部門等等。他們會給你一個
            非常詳細的技術解釋,但最終,他們不關心實質的風險,那是別人的事。就像那句法文說的,「
            我走之後,哪管洪水滔天」。這都是別人的問題,與我無關。這句法文很好描述了他們如何
            推卸責任。 羅傑‧羅伯遜:所以,我們和美國人民一樣,不知情地支持著那些製造洲際彈道導彈
            的中國公司,而他們的目標是我們的城市。我們的軍隊,我們的海軍居然投資於那些正在南海
            島嶼上建立軍事基地的公司,或者製造高超音速反艦導彈的公司。這就是為什麼美國海軍部長
            理查德‧斯賓塞,一個偉大的美國人,站出來說......他不是前任,他是現任海軍部長,他非常
            強硬地問:這是怎麼回事?我們必須為自己人負責。 我的意思是,這是常備軍,有自己的預算,
            當他們想搞海外投資的時候,雖然大多數多樣化的投資組合都包括跨國公司,但是軍隊只有
            一個選擇,那就是追蹤MSCI全球指數,沒有第二個選擇。有人暗示有,I基金會給你一些選擇
            。 羅傑‧羅伯遜:但是沒有選擇的餘地。不會有。當然,這還沒有實施,這是最好的消息。他們
            已經做出了決定。在這之前的三次董事會會議上,他們已經重申了這一決定。現在他們公開
            表示,女士們,先生們,事情將會是這樣的,我們堅持我們的立場。我們走著瞧吧。這個事還
            沒有結束。有相關的立法。在這個問題上有兩黨合作,還有行政部門的參與。我們會讓川普
            政府坐視不管嗎?川普總統的團隊,會投資解放軍公司和集中營嗎?有一些棘手的問題需要問
            行政部門和國會,但是國會已經站出來了,他們說,不,不,不,不要認為,你是董事會,不要認為
            你說了算。 第二部分:總統的立場 蕭茗:那總統呢?執行部門呢?他怎麼看這個問題? 羅傑
            ‧羅伯遜:我想他們正在研究這個問題。我認為他們意識到了這個問題。我認為他們正在就這個
            問題舉行會議。我認為在白宮和其他地方有一些人,比如海軍部長,他們非常關心這個問題。
            他們看到了這個事情的緊迫性,本來投資基金中只包括發達國家的公司,沒有新興市場企業,
            但是現在不僅包括中國和俄羅斯的企業,而且在俄羅斯方面,在摩根士丹利資本國際(MSCI)
            全球(除美國外)指數中,有五家俄羅斯公司受到美國財政部海外資產控制辦公室OFAC的制裁,
            OFAC的制裁措施是最嚴厲的。但是有人還是不當回事。 看,這些都是目前應該考慮的事情。
            我謹慎並樂觀地認為,川普政府會認識到這個問題的嚴重性和危害性。他們不會坐視這個事情
            在自己的眼皮底下發生,因為當這些擺在明面上的時候,任何行政部門無法迴避。 羅傑‧
            羅伯遜:你曾經參與過嗎?你曾經使用過你的行政權力嗎?我曾為一名叫羅納德‧威爾遜‧里根的
            總統工作過。我不了解川普政府和它的運作,但我非常清楚地了解里根總統對國際經濟和金融
            投資組合的看法,因為我曾經參與過里根政府的運作。我也知道,他在這個問題上是如何做的。
            如果里根總統在位,我們就不會有這樣的爭論,因為里根總統對聯邦儲蓄委員會來說會是一股
            不可戰勝的力量。他們就不會如此傲慢,在你剛剛讀到的信裡,他們公然叫囂要我們少管閒事
            。 蕭茗:談到川普政府對此的態度,我想知道川普的貿易戰和這有什麼關系?因為如果川普
            最終想要與中國達成貿易協議,想要美國和中國經濟繼續相關聯,這種努力不是會起到阻礙作用
            嗎? 羅傑‧羅伯遜:嗯,可以肯定的是,中國暗地裡向川普政府表明,他們想都不要想(採取)任何
            行動,即使只是執行現有的法律和法規,更不要說新的法規。如果他們試圖執行現有的遊戲規則,
            就會付出慘痛代價,包括在貿易投資組合中。看看NBA。 我們是不是可以這麼說,中共以敲詐
            勒索著稱,而他們......他們不會不好意思,至少在暗地裡,他們會確切地告訴你你的行為
            將會有什麼樣的後果。這是他們的慣用手法。所以我認為他們很可能已經傳達了這個信息,
            有些人聽進去了、對此感到擔心,因為這第一階段和以後的貿易協議在政治上和實質上都是
            非常重要的。 羅傑‧羅伯遜:我們收到這個信息了。另一方面,這不能成為對數千億美元的潛在
            用途視而不見的藉口⋯⋯這些錢從美國投資者那兒進入中國,被用於惡意的用途,即使不是反對
            我們,也是用於軍事現代化和政治軍事領域中有問題的活動、控制其它國家,還有很多其它
            五花八門的事情,踐踏著美國價值觀、踐踏個人自由和人民的自由。 我們應該是自由的
            維護者,我們應該是自由的燈塔。我們為什麼要允許我們的人民資助集中營和在西藏火車站
            使用面部識別技術?去幫助圍捕那些異見人士嗎?我們應該資助中國的社會信用體系,或者一個
            監控人民的國家,或者數字極權主義,或者任何這一類的東西嗎?你知道,這些都是違背美國
            價值觀的、令人憎惡的活動。華爾街不能把這些全部抹掉,假裝事實並非如此。 羅傑‧羅伯遜:
            警鐘已經敲響了。我不認為有人能把事情倒回去。沒有人能掩耳盜鈴。嘹亮的號角已經向全
            美國人民吹響,包括國會內兩黨的合作和很多主流媒體的報導。謝天謝地。這一切都從6月
            開始,從我們出版耗費兩三年努力得出的研究成果開始。 我們在今年3月開始公布這些成果。
            在這之前你什麼都看不到。現在你會看到這件事情在發展,其他人也在參與進來,其他對上市
            公司會計監督委員會審計方面非常了解的專家,多德‧弗蘭克法案方面的專家,以及理解將財務
            披露視為「國家機密」的後果的專家。換句話說,我們,包括我自己,都在關註這個問題的人權
            和國家安全方面。 羅傑‧羅伯遜:我是一名國家安全人員,但多年來我也一直積極參與人權事務。
            這是一方面。但是監管方也有問題。為什麼沒有要求信息公開?在透明度和風險管理,以及
            保護股票價值和企業聲譽方面又做了什麼?對法制的關注到哪去了?就算只是從仲裁的角度
            出發? 換句話說,良好的公司治理怎麼樣?公司監管是這個國家的首要任務。這個監管群體
            可能會非常強勢,他們總是為了維護公眾的利益而緊追華爾街不放。 羅傑‧羅伯遜:公司監管
            團體對此有何看法?一片沉默。 第三部分:監管機制出了什麼問題? 蕭茗:美國證券交易
            委員會呢? 羅傑‧羅伯遜:嗯,他們確實收到了大量關於這個事情的詢問。我認為他們將不得
            不做出反應。我認為,我們不應該容忍中國企業損害國家安全和踐踏人權,包括對這些令人
            憎惡的事情負有直接和間接責任的人。這個問題對這些企業的股票價值和企業聲譽構成重大
            風險,因為負面報導會損害股票價值,因為他們可能會被制裁或被列入實體名單,然後你會看到
            股票暴跌。美國人民有權了解這一潛在的風險。隱瞞信息對美國人民是不公平的。 蕭茗:
            您不認為幾乎所有中國公司都有兩三套會計記錄這一事實也應該揭露給美國投資者嗎? 羅傑‧
            羅伯遜:我同意,我同意。因為證券交易委員會成立於1933年,如果我沒記錯的話。它的核心
            任務是什麼?我認為,它的核心任務是確保針對股票價值和公司聲譽的重大風險應適當地披露
            給潛在投資者,使他們能夠做出更明智的投資決策。 所以如果你回到1933年,讀一下他們的
            委託書/授權令,我認為它大致上是這樣說的。因此,我認為證券交易委員會是主要的補救機構
            之一。但如果他們真的想解決問題,那就應該採取實際措施。我的意思是,他們為什麼對節儉
            儲蓄計劃投資中國公司一事保持沈默?這是一場災難。 蕭茗:所以他們什麼都沒說? 羅傑‧
            羅伯遜:一點都沒。所以你知道這是一個挑戰。再說一遍,我不想不公平。這是一個新問題,
            這是一個規模巨大的問題。 蕭茗:你知道嗎?我們聯繫了證券交易委員會,想採訪他們,但他們
            不理我們。 羅傑‧羅伯遜:我想即使你是CNBC(美國消費者新聞與商業頻道),他們可能也會
            忽視你。換句話說,我猜他們還沒有準備好。我希望這是因為他們正在研究具體的解決方案集,
            他們不想預告新的規則或新的執行措施。我的意思是,如果我們想對此採取最樂觀的態度,
            這也許是合理的。我當然希望如此。 這是一個新問題。正如我所說,它有一個巨大的後果。
            它涉及被管理的40萬到60萬億美元基金。我的意思是,美國的資本市場,我們要記住,有超過
            全球60%的流動資金。粗略地說,其規模相當於世界其它地區資本市場的總和。所以這是一個
            很大的問題,希望他們是在花時間理解這個問題,並搞清楚他們在哪些方面可以利用現有法律
            法規的執行措施,來加快解決這些可怕的不平衡問題。 蕭茗:他們確實給了一個藉口,說他們
            缺乏人力,缺少方法。他們說要解決這個問題,這個新問題,就像要用AK 47步槍擊落衛星
            。 羅傑‧羅伯遜:讓我先問觀眾,或者問你一個問題。 羅傑‧羅伯遜:為什麼美國的情報機構
            不與美國證券交易委員會聯繫,以便更好地了解這些中國和俄羅斯公司的背景?我的意思是,
            是的,很多資料都是公開的,我只在已公開資料的基礎上去研究。我沒有許可證。我沒有查閱
            祕密資料的權限,這對我來說正好。我過去當然有,但最近沒有。舉個例子,如果我仍然是國家
            安全委員會國際經濟事務的高級主任, 羅傑‧羅伯遜:有一天我將建立情報機構和美國證券交易
            委員會之間一種新的聯絡關系,這樣當我們審查進入我們市場的中國和俄國公司,無論是櫃臺
            證券交易市場,或者也有另一個很小的可能是紐約證交所的首次公開募股(ipo)......但是
            如果這種事情真的發生了,美國人民應該知道這些人是誰?他們有侵犯人權的歷史嗎?他們過去
            是否從事過欺詐活動?他們是知名的黑客嗎?他們的雇員有因間諜活動被捕的嗎?他們是解放軍
            的附屬機構或者南海島嶼的建造者嗎?他們對朝鮮的核計劃和導彈計劃有過貢獻嗎?或者為
            平壤和那個暴政國家輸過血、打過氣?(我們)尤其應從人權的角度來看。美國人民不是傻瓜
            。 羅傑・羅伯遜:(美國人民)了解這些事情,我相信他們希望自己的投資大體上符合他們
            最堅守的價值觀和原則。他們大多是愛國者,對侵犯人權有著強烈的義憤。我們是否真的相信,
            如果他們知道自己的投資資金落到了侵犯人權者手上,這些人不僅威脅著他們的家庭,還威脅
            著他們的社區、他們的城市、他們的州、他們的國家,我想他們會感到憤怒。現在有多少
            投資人?有1.5億人持有中國股票和債券。 還有數以百萬計的人持有俄羅斯政府認可的公司
            和主權債券。加州公務員退休基金也持有。 羅傑‧羅伯遜:4億6千萬美元俄羅斯的主權債券,
            我認為。等一下。什麼是主權債券?就是「我,俄羅斯政府給你一張有到期日和利率的紙,
            你給我幾千萬元甚至更多」。那我該怎麼處理這些錢呢?它就成了可自由支配的現金。我可以
            用它做我想做的任何事。我可以進一步破壞烏克蘭東部,我可以加強我在敘利亞的軍事部署,
            我可以有錢開發最新的超音速巡航導彈,它可是有核彈頭的,我還可以建造新一代彈道導彈
            潛艇。 羅傑‧羅伯遜:您知道,我們曾經有一種稱為自由債券的東西為第二次世界大戰提供資金。
            我們現在在幹什麼?我們現在在從事什麼事業?反自由債券?這就是我對它們的看法。反自由
            債券。嘿,讓我們用收益來粉碎自由。現在,您是否真的認為這個問題將消失或者再被掩蓋20
            年?我不這麼認為。 我認為這直接挑戰我們美國人的核心價值觀。而且,我們不會聽信這些人
            對受託責任的狹義上的解釋,因為他們得到了報酬,比方說一艘額外的遊艇,用於週末在漢普頓
            度假。 換句話說,這在很大程度上也與貪婪有關。我們不用把他們看成無私的,很棒的人,
            他們當然要考慮投資者的利益,但他們也關心自己的利益。這一點我們要弄清楚。 我們曾經
            有一種稱為自由債券的東西為第二次世界大戰提供資金。我們現在在幹什麼?我們現在在從事
            什麼事業?反自由債券?這就是我對它們的看法。反自由債券。嘿,讓我們用收益來粉碎自由。
            現在,您是否真的認為這個問題將消失或者再被掩蓋20年?我不這麼認為。 我認為這直接挑戰
            我們美國人的核心價值觀。而且,我們不會聽信這些人對受託責任的狹義上的解釋,因為他們
            得到了報酬,比方說一艘額外的遊艇,用於週末在漢普頓度假。換句話說,這在很大程度上也
            與貪婪有關。我們不用把他們看成無私的,很棒的人,他們當然要考慮投資者的利益,但他們也
            關心自己的利益。這一點我們要弄清楚。 蕭茗:告訴我為什麼?為什麼他們要這樣做? 羅傑‧
            羅伯遜:我確實相信了。 羅傑‧羅伯遜:好吧,你看,我是資本主義的忠實信徒,並且我是華爾街
            的國際銀行家。我從大通曼哈頓開始我的職業生涯,當時這家銀行的股票就屬於藍籌股。因此,
            我不反對賺錢和搞金融創新。但是這裡涉及到的利益是不同的。我的意思是,有許多賺錢的
            方法,但不是什麼錢都可以賺。你知道,黑手黨喜歡賺錢。三合會喜歡賺錢。 關鍵是我們不想
            在這裡引入我們的價值觀,我們在工作上就不去考慮這些價值觀,並認為我們不必再為國家或
            國家安全而擔心。而且,我們不必擔心集中營和侵犯人權行為。換句話說,(並非好像)「什麼
            錢都可以賺」。 羅傑‧羅伯遜:我不這麼認為。我認為您需要真正的監管。我相信你有自己的
            原則。您想維護自己的聲譽,避免採用不正當的方式牟利。那是我的觀點。我認為這是大多數
            美國人的看法,這就是他們的期望。您知道,投資人依賴基金經理,包括那些投資於在交易所
            上市的基金或所謂的指數基金,甚至共同基金等等的投資人。他們並沒有參與投資的過程,他們
            不懂如何在數百甚至數千家公司的股票中選擇。那不是他們的工作。他們相信自己的財務顧問
            ,基金經理,各行各業的資產經理能夠正當的,正確地做出投資選擇,並且合理的預估投資風險,
            而不僅僅是看重投資回報。系統的崩潰就在這一點。造成這種情況的部分原因是,中國占了20
            年的便宜,他們看到我們如此大意,即使是受制裁的中國公司也不會受到懲罰。 羅傑‧羅伯遜:
            我的意思是,即使他們在受制裁的實體名單上,也不會在這方面受到懲罰。好吧,哪一方面呢?
            他們正在獲取的數萬億美元的資金。錢。如果您認為貿易比金融重要,不妨再想一想。 蕭茗:
            請您估計一下中共對美國資本市場的滲透程度? 羅傑‧羅賓遜:我看過某單位從三個方面作出
            的估計。這個問題不好判斷。很難估算資本市場上出售的債券的價值。因為以美元計價的債券
            ,在法蘭克福、香港、新加坡發行,但是這些債券最終都被美國的投資銀行,通過海外的二級
            市場收購到了美國。所以這是個複雜的問題。相信我,我曾經嘗試過。我的估計是,上市資本
            或者股票的規模有1.9萬億美元,另有高達1萬億美元的債券。美國每年的國防經費是7千億
            美元。想像一下兩者之間的差距。前者只是後者的1/4。 蕭茗:是的,中共的整個外匯儲備有
            3萬億美元。一帶一路耗資6千億美元。 羅傑‧羅伯遜:他們怎麼會有看起來幾乎是無限量的
            資金,在東南亞或者地區來買下這些國家,或者買下非洲大陸,或者買下拉美的一些地區呢?
            他們哪裡來的無限的錢擴充軍備,以至於幾乎成了美軍的對手? 蕭茗:這很諷刺。只有中國有
            條件搞一帶一路。美國負擔不起一帶一路這樣的計劃,中國能,但是中國的錢怎麼來的,對吧
            ? 羅傑‧羅伯遜:人們再次說:「呃,你知道,如果美國執行現有的法規和證券法,哦,你看著吧。
            中國會去別的地方,他們會去倫敦,法蘭克福,新加坡,香港。而我們會搬起石頭砸自己的腳。
            我們的市場不會再那麼有競爭力。我們會把這個買賣拱手讓給別人。」我聽過很多這種說辭
            。 蕭茗:嗯。 羅傑‧羅伯遜:美國的資本市場無可替代。當今世界上可以用來投資的資金
            一多半在我們這裡。法蘭克福、倫敦,或者新加坡的資本市場只能滿足中共幾個月,而不是幾年
            的資本需求。那些市場的規模有限。他們沒有那樣多的流動資金來支撐中共對美元的巨大需求。
            所以記住吧,(中國)沒有別的地方可去。 蕭銘:所以,如果中共被趕出美國資本市場,您認為
            中共會怎麼辦? 羅傑‧羅伯遜:我認為中共不會被完全趕出美國的資本市場。我不提倡把中國
            大陸——世界上第二大經濟體從資本市場排擠出去。它需要在資本市場擁有相應的地位。就像
            在貿易領域那樣。我認為大多數人不會不切實際地要求終止一切貿易活動。我們要的是自由
            和公平的貿易。我們要的是不會威脅到國家安全,也不會踐踏美國價值觀的貿易,包括人權領域
            的理念。我們也會在資本市場上秉承同樣的原則。 你知道,如果一個自行車製造商想在紐約
            融資,我不會睡不著覺。如果是解放軍的先進武器製造商來做同樣的事情,那就完全是另一回
            事了。 如果我們尋求投資回報,我們就應該確保投資的對象是良性的、商業性的,在我們根本
            的國家安全與我們的愛國主義情感這些方面和它沒有衝突。 如果我們尋求投資回報,我們就
            應該確保投資的對像是良性的、商業性的,在我們根本的國家安全與我們的愛國主義情感這些
            方面和它沒有衝突。 羅傑‧羅伯遜:也包括我們的價值觀、原則和道德準則。為什麼不能把
            這些一起考慮呢?為什麼我們不能把這些生命中明顯的里程碑作為指導呢? 羅傑‧羅伯遜:但是
            如果在一定程度上限制中國進入美國資本市場,就會把中國大陸的經濟增長率砍掉一兩個
            百分點。如果你以為中國現在已經處於困難時期了,不妨想像一下在那種情況下會是什麼樣
            。 北京焦慮的希望保持現狀,他們威脅任何想改變現狀的人。所以會不容易。改變是需要
            勇氣的。我覺得川普政府有這樣的勇氣。我希望如此。他已經在其它地方表現出了這樣的勇氣。
            所以剩下的就是教育人們,讓他們豁然開朗,用普通人的邏輯能夠理解。就像我們今天的談話
            一樣。 羅傑‧羅伯遜:這個不奇異,不高科技。這是我們在喝茶飲酒的時候就能談的話題。每一
            位美國人都應該為自己呼籲。他們應該去他們的財務顧問,理財經理,和退休計劃經理那裡問:
            我有中國投資嗎?我有俄國投資嗎?告訴我我持有哪家中國公司的股票?你有這些公司的介紹嗎
            ?我可以看看他們的子公司做什麼嗎?你能給我他們的子公司名單嗎?您能告訴我他們是否曾經
            受到制裁或者現在還受到制裁?他們曾經被指控侵犯人權,黑客入侵或腐敗嗎?您能告訴我,我
            投資的這些公司的一些情況嗎?您知道一貫的答案是什麼嗎? 蕭茗:什麼? 羅傑‧羅伯遜:「我
            不知道。我不知道。我不是被僱來做這個的。」錯。是的,你是被僱來做這個的。是的,你是。
            我會去找會做這件事的人。那就是下一步。那是普通美國人有權站出來說話的地方。 去見見
            國會議員,去見參議員,到白宮和財政部和證券交易委員會去問:「為什麼我得不到保護?
            為什麼會出現這個爭議?你知道,這個人在採訪中說了什麼?他說的對嗎?是真的嗎?」 第四
            部分:貿易不是真正的戰場 蕭茗:請您告訴我,美中貿易和美國對中國公司的投資,哪一個更
            重要? 羅傑‧羅伯遜:貿易是美中關係中一個搶眼的問題。他們(中共)能應付貿易戰之類的
            問題嗎?是的,這對他們有些痛苦,但是,他們能,他們能一直玩下去。看看那些事情起落吧。
            你知道的,你沒有看到他們有任何驚慌失措。他們只是把貨幣貶值或者做些其它事情來抵消
            關稅的負面影響。他們也認為我們的農民和其它受害的經濟部門會對川普施壓,起到掣肘的
            作用。換句話說,他們把這些事情玩到了很深的程度。 當我們來到高技術領域時,他們就不
            那麼喜歡了。那可不是這麼舒服的。他們不希望我們從保護國家安全和人權的角度出發,去
            調查海康威視、中興、華為和其它企業。但是他們能忍受那種局面,因為對中興的制裁有條件
            的解除了,他們也在計劃讓華為免於制裁。他們甚至在努力把「曠視科技」從實體名單上拿掉
            ⋯⋯人工智能。也就是說他們可以辦得到。我來告訴你他們最怕的是什麼⋯⋯缺錢,被趕出美國
            資本市場。因為能否繼續從美國資本市場融資關係到中共政權的存亡。 蕭茗:您曾是里根
            總統的經濟顧問。里根時代和現在有什麼相似之處嗎?有沒有我們可以從那個時代學習借鑒
            的經驗? 羅傑‧羅伯遜:里根總統有好萊塢背景,就像川普總統有房地產背景。你知道里根總統
            曾經擔任美國最大的州的州長好幾年,這是他的優勢。而且他在幾十年裡一直在關注我擅長的
            這個領域,包括外交政策、國家安全問題等。在他為通用電氣公司做發言人時曾經親自撰寫
            發言稿,表示他一直在擔憂共產主義。他是反共干將。在他做演員行會會長時曾直接被他們
            威脅恫嚇,當時正逢共產主義努力滲透好萊塢,他在那個系統裡面阻止了他們,於是他們到他
            家裡威脅要往他臉上潑酸等等。他有這些故事可講。 羅傑‧羅伯遜:他有第一手經驗而且對此
            很有研究。所以他知道共產主義者、共產主義和威權主義的特性。所以里根和川普的背景確實
            不一樣。可以肯定川普總統也有很多優點。他在貿易上採取了大膽的步驟。在技術領域他阻止
            了與軍事相關的技術出口中國,這是其他總統沒有採用的大膽步驟。 他情願激怒北京,而
            大多數人則過於小心。結果是中共得到了他們想要得到的一切,包括在資本市場。這就是
            為什麼我們現在一團糟,某種意義上講,如果你不想留情面,可以說是因為我們在事實上採取了
            某種綏靖政策。有人說這完全是出於包容,希望我們與他們建立商業關係等等能讓他們的態度
            變得更加多元化,在地緣政治上更加合作。我們與蘇聯緩和關係時也抱有同樣的幻想,而且如同
            (現在)這個一樣破滅了。於是才有了我們看到的勇氣。 但里根很有內涵。 他對善惡有很深
            的理解。他不是無緣無故講出「邪惡帝國」的。他發明了這個詞。他把這看作道德選擇。 我
            們所珍視的價值觀、原則和所有東西對他影響巨大。他知道這些共產主義威權和獨裁者們想要
            把我們的這些都打碎,他下定決心,只要他當權就不會讓這些發生。他感興趣的不是僅僅讓蘇聯
            遇到更多的困難。他感興趣的不是僅僅在某個領域占上風。他感興趣的是徹底擊敗蘇聯,而這
            正也是他著手去做的。 我有幸參與了我們的一項經濟和金融戰略,我是構架它的人。我們針對
            的是他們的硬通貨的現金流量,支撐他們持續成為我們威脅的貸款,那些西方國家對他們生命線
            的支撐。 蕭茗:告訴我那天的情景。就是你和總統坐下來決定如何對付蘇聯的那一天。 羅傑‧
            羅伯遜:好吧,我和他最好的朋友,國家安全顧問威廉‧B‧克拉克(William B. Clark)一起
            去了橢圓形辦公室,我列出了計劃如何針對他們包括現金在內的硬通貨資金流,包括針對他們
            銷往西歐的天然氣,儘力阻止西伯利亞天然氣管道項目和其它項目。事情將產生巨大的變化,
            那些讓莫斯科的硬通貨收入增加一倍,並使西歐超過75%的國家依賴蘇聯天然氣(這是他們肯定
            會用來分裂北約的槓桿)的事情將改變。 換句話說,這是一個複雜的故事,但已針對如何處理
            這一問題制定了補救計劃。蘇聯每年的支出比收入多160億美元。所有這些資金都是由西方
            政府和銀行提供的。這恰好等於外部蘇聯帝國的硬通貨成本。他們用盧布做很多。它們在貿易
            方面做很多,但是硬通貨部分是用美元和日元。你知道硬通貨幣的含義。因此,總的來說,我
            基本上對他說,我們每年要為蘇聯外部帝國的硬通貨需求提供100%的融資。不是10%,而是
            100%。 羅傑‧羅伯遜:我們談到如何降低油價,讓沙特阿拉伯每天偷偷多抽出200萬桶的石油,
            放寬美國這裡的井口的價格,使石油價格跌至每桶10美元,因為他知道每桶石油價格每下跌
            1美元,蘇聯人將損失大約10億美元。他們一年只賺320億。 我的意思是,就現金流量而言,
            我們把他們像火柴棒一樣打碎了。克拉克法官問總統:您想怎麼做?總統說,基本上,「我不
            在乎你怎麼做」。他在開玩笑是因為他確實在乎怎麼做,然後他說,「去做吧」。 蕭茗:就
            去做,就這麼簡單。然後就實施了。這是一個祕密計劃。是個祕密,對吧? 羅傑‧羅伯遜:全
            美國12-13個人知道此計劃。 蕭茗:在他的操控下花了多長時間基本上終結了蘇聯? 羅傑‧
            羅伯遜:大概18個月吧。兩年。事情逐漸成型。蘇共摸索著,強撐著又走過了另外七年,想要
            設法渡過難關等等。但關鍵是他們已經無力回天了,只不過這個過程是有意拖長的,所以蘇共
            不會覺得無路可退,在核武器方面沒有感到那麼大的壓力。在開始的時候,情況看起來好像還
            不是那麼嚴重。 我們需要這是一個緩慢的,逐漸的崩潰。 因此,在蘇聯解體之前的幾天,他們
            960億美元的西方債務違約了,您可以問問自己,親愛的,這兩件事可能有聯繫嗎?是有聯繫的。
            看,有很多因素。軍備競賽使他們的經濟不堪重負。技術方面,我們的SDI嚇壞了他們。 羅傑‧
            羅伯遜:事實是,無論在哪裡,我們都在任何地方挑戰它們,從毒刺導彈到聖戰者組織,再到在
            尼加拉瓜的採礦港,我們到處對付它們,增加他們的成本。 羅傑‧羅伯遜:我們通過告訴聯合國
            和其它組織蘇聯真正的面目,發動了一場理念之戰。我們向歐洲部署了潘興(Pershings)和
            巡航導彈,飛到歐洲只要6分鐘,以此證明我們不會接受它們的SS20導彈的威嚇。因此,該計劃
            包含許多要素,但歸根結底,經濟和金融方面的對策起了核心作用。 蕭茗:你知道,中國的經濟
            比蘇聯大得多,現在美國和中國的經濟交織在一起。您認為這種策略今天仍然有用嗎? 羅傑‧
            羅伯遜:中國幾乎沒有緩衝有人會說,他們在經濟增長低於7%的時候就處於慢動作內部崩潰
            狀態。而且他們的承受能力遠遠超出他們所說的。顯然,他們的房地產泡沫不會消失。他們的
            不良貸款問題一直存在,而且一直沒有消失。問題非常嚴重。他們很脆弱。他們喜歡將自己
            描繪成一個無敵的巨無霸,並且喜歡炫耀自己3萬億美元的外匯儲備等。順便說一下,其中一些
            已經在流通裡,或者是投在了非洲等地的股票裡。它不是馬上能用的現金,當然,這是另一個
            討論了。 羅傑‧羅伯遜:但是他們和金錢一樣脆弱,僅此而已。他們沒有可兌換貨幣。他們希望
            像他們所說的那樣去美元化。但是在可預見的將來,我們是世界的儲備貨幣。 羅傑‧羅伯遜:
            你就是無法揮舞魔杖說:「我不要美元了」。因為美元是唯一的世界貨幣。 羅傑‧羅伯遜:這是
            美國在21世紀的世界上最後的、近乎壟斷的資產之一,就是美元。 曾幾何時,對於蘇聯,我們
            的石油和天然氣設備和技術是唯一可以通過西伯利亞永久凍土的技術。您知道,我們利用這種
            槓桿作用是因為我們在那裡壟斷了,這是一個很長的故事,但是當您談論阻遏極權主義者的
            統治,維護自己在世界上的主導地位時,這些才是真正重要的事情。因此,我很樂觀地認為我們
            將完全主導這個星球上的經濟和金融領域。 羅傑‧羅伯遜:我相信我們控制世界上大部分的
            流動性資本。我只是認為我們還沒有醒來。 蕭茗:就是這個問題。美國願意這麼做嗎?我的
            意思是,現在是兩個經濟體。中國對美國資本市場的滲透如此之廣,如此之深,你是否覺得現在
            改變這些太晚了? 羅傑‧羅伯遜:不,不晚。我認為這是一個合理的問題,也是一個令人高度關注
            的問題,因為這一直是迄今為止流行的論點,並且在我們這裡時盛行。 羅傑‧羅伯遜:這是人們
            廣為爭論的,但有一個還未浮現的因素。 羅傑‧羅伯遜:這就是美國人民的認識程度。以我拙見
            ,美國人民還沒有明白過來。他們還沒有理解這場美中對決的性質和意義。 他們將找出答案
            ,至少我將盡我所能來確保他們了解這些事實,而不是觀點,經驗事實,並且當他們看到這些時,
            我想我了解我的美國同胞們,無論是強硬的國家安全支持者還是人權衛士,無論他們在政治光譜
            處於何種位置,他們都受到了不公正的待遇,而我們可以主動去告訴他們是怎麼回事。當他們
            發現這關乎他們的錢,而不是什麼抽象的東西,是他們自己的錢,你猜會怎麼樣?他們會把這
            當成自己的事。我就是要讓他們這樣去看問題。
            '''
        ),
    )
    assert parsed_news.category == '世事關心'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1576166400
    assert parsed_news.reporter is None
    assert parsed_news.title == '羅賓遜:美資本市場是中共生命線'
    assert parsed_news.url_pattern == '19-12-13-11719537'
