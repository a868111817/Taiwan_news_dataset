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
    url = r'https://www.epochtimes.com/b5/13/3/3/n3813123.htm'
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
            天主教教宗本篤十六世2月11日突然宣佈將於2月底退位,震驚全球,成為
            600年來在世時辭職的第一位教宗。 新的繼任者不僅將要面對一個因醜聞危機而令世人漸
            失信心的羅馬天主教會,還要應對越來越世俗化的新教運動帶來的挑戰。 本篤十六世宣佈
            辭職數小時之後,梵蒂岡聖伯多祿大教堂的屋頂遭閃電擊中,冥冥之中或有徵兆?一份12世紀
            的手稿預言指,新選出的教宗將是天主教末代教宗,然後是審判日將到來...... 1、教宗退
            位羅馬教廷何去何從 文 楊采華 教宗本篤十六世(Pope BenedictXVI)以年事已高、身體虛
            弱為由提出退位,他是六個世紀以來第一位提出退位的教宗。本篤十六世稱,在上帝面前捫
            心自問,感覺自己無力再帶領全世界10億多的天主教徒。 這一任務將由繼任者肩負,這位繼
            任者不僅將要面對一個因醜聞危機而令世人漸失信心的羅馬天主教會,還要應對越來越世俗
            化的新教運動帶來的挑戰。 天主教會多事之秋 近年來,羅馬天主教會面臨多事之秋。除了
            教宗管家洩密高層權鬥貪腐、神父性侵兒童醜聞困擾外,教廷對墮胎、同性婚姻議題立場保
            守,更屢屢引發輿論挑戰,信徒也似乎因而日漸流失。這些外在壓力,恐怕和本篤十六世(Pop
            e Benedict XVI)宣佈退位不無關聯。 《華盛頓郵報》日前刊登調查報導,聲稱梵蒂岡教廷
            高層權鬥貪腐嚴重,矛頭直指教廷第二號人物、國務卿貝托內(Tarcisio Bertone)。報導指
            控貝托內妨礙教宗推行改革,教宗管家加布瑞萊(Paolo Gabriele)有機會讀到相關信件,看
            不過去,決定向媒體「曝料」,曝光出「教廷洩密」(VatiLeaks)醜聞事件,牽連至少兩名
            教廷高層「明升實貶」的內幕。 報導中稱,時任梵蒂岡祕書長維加諾主教(Carlo Maria Viga
            no),因協助教皇推動教廷內部改革而四處樹敵,求助教宗和國務卿貝托內不果,義大利傳媒
            又散播對其不利的文章。貝氏附和傳媒的批評,撤去其職位。之後還將他調離梵蒂岡,轉任
            教廷駐美國大使。 維加諾隨後向貝托內寫信表達不滿,指責貝氏妨礙教宗下達的改革任務:
            「我這次調職,將令本來相信可將教廷多個部門貪污濫權行為連根拔起的人,大感迷惘和沮
            喪。」並直言懷疑教宗被「蒙在鼓裡」。 管家加布瑞萊說:「目睹邪惡和腐敗充斥在教會
            之中,我終於達到了墮落的臨界點,從此難再回頭、無法自控。」加布瑞萊受到審判, 並被
            判入獄。他在獄中度過幾個月後,教宗親自將其赦免。 此外, 截至2010年3月, 有六國的天
            主教會遭到性侵指控,教宗本篤十六世向媒體表示,神父性侵兒童案讓他感到「震驚和悲不
            可抑」,並承認教廷警覺性不足,後續行動也不夠果決。 2008年底,本篤十六世在教廷發表
            年終演說時指出,性別理論模糊男女之別, 同性戀威脅人類生存,其嚴重程度不下於氣候變
            遷。教宗這場談話隨即引起捍衛同志權益團體的強烈不滿。 最後一場公開彌撒籲終結「宗
            教偽善」 羅馬天主教教宗本篤十六世13日主持辭職前最後一場公開彌撒,呼籲天主教會終
            結「宗教偽善」和「對立」, 滿場信徒給以如雷掌聲,場面動容。 85歲的本篤十六世當天
            先到梵蒂岡一個會堂,進行每週公開接見信徒活動,獲在場約8,000名群眾鼓掌歡呼,有信徒
            更拉起「謝謝教宗」的橫額致意。 教宗精神不俗,毋須攙扶下仍能自行步往主禮座席,隨後
            以響亮聲音發表演說。 他再次說明退位的理由:「我在長時間祈禱並以良知在神前思考後,
            為了天主教會的利益,做出了這個全然自由的決定。」 本篤十六世表示,他「十分瞭解這個
            做法的重大性,但也明白,他無法以所須的體力和精神來履行教宗聖職」。 戴上主教冠、披
            著紫色袍子的教宗在最後彌撒中,呼籲信徒更加真誠。他譴責「宗教偽善」,並呼籲終結「
            個人主義」和「對立」。 他說:「教會的顏面......有時會受到損害。我想到的特別是反
            對教會團結的罪惡。」他指的可能是教會捲入的許多醜聞。 彌撒結束時,現場掌聲響了好
            幾分鐘,教宗明顯感動。他說:「謝謝你們。現在,讓我們回到禱告吧。」接著他離開聖伯多
            祿大教堂(St Peter’sBasilica),向信徒微笑揮手。 本篤十六世是全球12億天主教徒的
            領袖,也是天主教會2000年歷史上第二位自願請辭的教宗,以及約600年來首度在有生之年請辭
            的教宗。他將於本月28日卸任,梵蒂岡宣佈,樞機主教會議將自3月15日至19日之間召開,以
            選出繼任教宗,並將爭取在復活節前選出本篤十六世的繼任者。 據悉,今次參與投票的樞機
            共117人,經過多輪投票後,票數達三分之二大多數者,當選為新教宗。 如果選出新教宗,
            梵蒂岡西斯汀小堂的煙囪會冒出白煙,聖伯多祿大殿大鐘同時敲響。選出教宗後,樞機主教團
            代表會在聖伯多祿大殿陽臺上,宣佈結果。 無論本篤十六世的接班人是誰,他都必須針對目
            前天主教會面臨的五大議題提出對策:避孕和愛滋病、教會內部性侵、同性戀及同性婚姻、
            墮胎、女性地位。 前臺灣駐教廷大使:權力鬥爭是無稽之談 據臺灣前駐教廷大使杜築生在
            發表的一篇文章中回憶道,2010年,教宗曾接受德國名記者史瓦德(Peter Seewald)長達數周
            的專訪,談話內容包括:社會對教宗的責難、神父性侵兒童對教會的傷害、教會的改革、今日
            信仰與理性的結合、墮胎、氣候變遷、同性結婚、世界經濟危機、新無神論、基督徒合一、
            天主教與穆斯林的關係以及教宗對和平的展望等問題。 史瓦德當時尖銳地提問:教會
            今日遭遇層出不窮的問題,請問有無考慮過辭職的事?教宗回答:災難發生時,不能逃避,也不
            能委諸他人,必須親自處理;等到風平浪靜或實感無以為繼時,才是時候,故此刻不是辭職的
            時機。史瓦德追問:可否想像,在何一情境下才是教宗合宜辭職的時刻?教宗回答:倘若一位
            教宗清楚地瞭解,他在體能上、心理上以及精神上不能再恪盡職責,則他有權利,且在某些情
            況下還有義務辭職。 杜築生因此認為,教宗退位係陰謀論或教廷權力鬥爭的傳言,實在是無
            中生有、唯恐天下不亂的無稽之談。 這位前教廷大使對現任教宗的印象是:本篤十六世是
            位學者、神學家,曾經出版了十餘冊的靈修及神學巨作。他與前任教宗是完全不同的典型。
            保羅二世(又譯若望保祿二世)是位和藹可親的長者,他喜歡親近、擁抱信眾。 本篤十六世
            是位學貫古今的大學者,信眾需要傾聽他的教誨才能欣賞他。他喜愛在森林中散步,坐在鋼
            琴前彈奏巴哈的樂曲,他最大的樂趣是提筆著書。但教宗公務繁忙,因此不得不暫時放棄喜
            好。 哥哥:確實因年紀大了力不從心 退位後不會干政 教宗本篤十六世的哥哥
            約格奧爾格.拉辛格(Georg Ratzinger)89歲,在接受BBC採訪時表示,教宗一旦退位後
            絕不會干涉繼任者的工作。 教廷發言人稱, 教宗離任後不再插手教廷事務;代表教宗權力的
            標誌,包括用作教宗印鑑的信物漁人戒指也將銷毀。 約格奧爾格還說,他弟弟要退位沒有
            其它意思,完全是因為年紀大了,前任沒有幾個活到他這個歲數,而且他覺得正在慢慢失去擔任
            教宗所必須的能力。 約格奧爾格對德國媒體表示,85歲的教宗早已行走困難,並且醫生已經
            建議不要再做洲際旅行,教宗在幾月前就已決定辭職。 本篤十六世出生於德國,原名
            拉辛格。早在2002年,時任梵蒂岡行政長官的拉辛格曾經以75歲高齡請求辭職。這位紅衣主教
            對當時的教宗保羅二世說,想作為退休人員享受幾天清淨的日子,用來寫幾本書。但這一請求
            被保羅二世拒絕。三年之後,保羅二世辭世,拉辛格在年近80歲時被選為第265屆教宗,他卻
            接受了這一選舉結果。 天主教教廷梵蒂岡發言人也坦承,即將退位的教宗幾年前便已經
            安裝心律調節器,幾個月前還曾做手術,替調節器更換新的電池。 拉丁美洲信眾多教會面臨
            當今所有挑戰 拉丁美洲一直被視為天主教徒迅速「增長市場」,42%天主教信眾來自
            拉丁美洲。教會中有不少人稱新教宗應代表信徒快速增長的地區。但是多方面看來,拉丁美洲
            聚集了教會在全球範圍內面臨的挑戰。 猶如其它地方一樣,該區域社會世風日下。在墨西哥城
            南部的聖母天主教堂內一位76歲的信徒維拉貴茨(Celia Castro Velzquez,)感歎,神職
            人員大量減少,她將此歸咎於道德標準的下滑。她說:「今天這一代年輕人只喜歡足球和
            摔跤。」 天主教教徒精神層面的堅信不如表面看得那麼堅定,往往摻雜了零星的民間
            信仰。 例如,在墨西哥,一個名為「聖亡」(Santa MUERTE)的邪教組織正在普及。位於
            墨西哥中部墨西哥城的一間「聖亡」社殿,內有披著黑色長袍、真人大小的骨骸放在玻璃櫃
            供人膜拜。 這種現象不僅在墨西哥,在其它地方也出現了。去年,教宗本篤十六世到訪古巴的
            時候,正好是加勒比海非裔宗教Santer稱的愛神400週年紀念日。 最近,天主教已經被
            Evangelists侵蝕。1980年代,這個不奉行天主教傳統教義的教派在因城市化迅速發展而
            造成的貧民窟中廣泛傳播。在巴西,近四分之一人口是Evangelists信徒。 另外,
            Pentecostalists深深地吸引那些希望在有生之年求得救贖的信徒,他們計劃花費2億美元
            模仿聖保羅的所羅門聖殿,建造一個可容納1萬人、18層高的殿堂。 巴西著名神學家
            艾利森(JamesAlison)說:今天,在拉丁美洲的政治機構往往對教會不再像人們認為的那麼
            恭敬。不像在英國那樣,教會是國家重要的一部分,也不
            如美國那樣,宗教在政治中仍扮演核心角色。 這樣的結果之一,是同性婚姻在重男輕女的文
            化中快速傳播。 這些因素是否足以使樞機主教選擇拉丁美洲教宗?即使是一些主要候選人─
            ─如管區中有600萬信眾的聖保羅大主教、63歲的紅衣主教謝勒(OdiloPedro Scherer)都不
            確定。 紅衣主教謝勒在慶祝聖灰星期三之前,輕輕擊破了下一任教宗應該來自發展中國家
            的假設。 他說:教宗選舉考量準則不在於是否來自於同(我們)一個地方或另一個地方,也不
            在於哪個原籍,更重要的是能否在這一歷史時刻中有帶領教會的最充分準備。 2、「末世教
            宗」預言手稿再獲關注 文 海寧 本篤十六世2月11日意外宣佈辭職,在幾個小時之後,梵蒂
            岡聖伯多祿大教堂的屋頂遭閃電擊中,正如本篤十六世突然辭職一樣,讓人有一種「晴天霹
            靂」的感覺,也有人認為這是不祥的預兆。 古羅馬人藉由觀察飛鳥、隕石和閃電來決定天
            神宙斯對國事的看法,而一份12 世紀的手稿預言,下一位教宗將是天主教末代教宗,然後審
            判日將到來。 《今日美國報》引述氣象學家法洛(Jesse Ferrell)的話說,雷電擊中聖伯多
            祿大教堂的照片應該是真實的,因為它是由專業攝影師所拍攝的,還有影片作為佐證,而且羅
            馬當天確實有發生雷雨。 「閃電襲擊」在羅馬有長遠而且具有象徵意義的歷史。一名閃電
            專家表示,古羅馬人藉由觀察飛鳥、隕石和閃電來決定天神宙斯對國事的看法。就閃電而言
            ,他們會觀察閃電發生的地點和方向,作為宙斯神是否同意的象徵。 「教宗預言」記錄最後
            112位教宗影像 一份12世紀的手稿預言,這位新選出的教宗將是天主教末代教宗,然後審判
            日將到來。這份叫做「教宗預言」(Prophecy of thePopes)手稿的真實性能否再次應驗重
            新受到關注。 「教宗預言」又稱聖馬拉奇(Saint Malachy)預言,據信由12世紀愛爾蘭主教
            聖馬拉奇撰寫。據傳他曾在1139年到羅馬訪問,看到了關於未來的異象及最後審判之前112
            位教宗的影像。他把這些異象以及一長串隱晦的短語寫在五頁羊皮紙上,交給當時的教宗依
            諾增爵二世。 預言裡沒有留下未來教宗的名字,而是描述人物特徵,或是有關國家、臂章、
            勛章等線索的暗喻。教宗讀了之後密封在教廷檔案館裡。原始手稿就此被人們忘卻,直到15
            90年被人重新發現。 然而這份手稿在正史中卻沒有任何記載。聖馬拉奇的傳記也沒有提到
            這個預言。有人認為這個預言是16世紀晚期的偽作,其真實作者是諾查丹瑪斯,假托於聖馬
            拉奇,以免因預言天主教的毀滅而受到責難。此預言的支持者則表示,即使今人不能確定預
            言的作者,預言仍然是有效的,理由是該預言曾準確預測多名教宗的背景和來源。 在「教宗
            預言」中,對依諾增爵二世之後下一位教宗的預言是「臺伯河上的城堡」。而塞萊斯廷二世
            (Celestine II,1143~1144年在位)就出生在臺伯河邊的一座城堡裡。 盧修斯二世
            (Lucius II,1144~1145年在位)。對他的預言是「被趕走的敵人」。這位教宗在任期中
            被趕出羅馬。 葛瑞戈裡八世(Gregory VIII,1187年在位)。對他的預言是「聖羅蘭
            之劍」。這位教宗的紅衣主教徽上有兩把劍。1187年,耶路撒冷被伊斯蘭教教徒攻陷。葛瑞戈
            裡八世發出教令,籲基督教世界拿起劍來,奪回聖地。 克雷蒙四世
            (Clement IV,1265~1268年在位)。對他的預言是「沮喪的龍」。這位教宗在西西里王位
            爭奪戰中和法王的弟弟查理聯手擊敗來自德意志的曼弗雷德,而曼弗雷德的家徽正是
            龍。 塞萊斯廷五世(Celestine V,1294年在位)。 對他的預言是「孤獨的生活」。他
            曾是生活在山中的隱士,在當了幾個月的教宗後辭職又回到了隱居生活。他是有史以來從教宗
            任上退位的第一人。 保羅四世(Paul IV,1555~1559年在位)。對他的預言是「彼得的
            信心」。這位教宗登基前名叫彼得.卡勒( Carafe)。Carefe
            是信心的意思。 烏爾班八世(Urbain VIII,1623~1644年在位)。對他的預言是「百合與玫
            瑰」。他出身的義大利佛羅倫斯教區以百合花為象徵。烏爾班八世在其徽章中用了三對採
            集百合和玫瑰花蜜的蜜蜂。 亞歷山大七世(Alexandre VII,1655~1667年在位)。對他的預
            言是「山峰的守門人」。其家徽的中心位置是一座山峰。 本篤十五世(Be n e d i c t XV
            ,1914~1922年在位)。對他的預言是「苦難的宗教」。他的任期經歷了西班牙大流感和蘇俄
            十月革命,致使天主教會不但人丁減少,威信也受到了很大的打擊。 步入現代,約翰.保羅二
            世(JohnPaul II)成為預言中的第110位教宗,也就是倒數第三位教宗。對他的預言是「太陽
            的事工」,又可譯為「日食」。這位教宗的出生日和葬禮日都逢日食,這種事件的機率非常
            小。 預言中的倒數第二位教宗正是剛剛宣佈退位的本篤十六世(BenedictXVI)。對他的預
            言是「橄欖的榮耀」。德國紅衣大主教拉辛格當選後,大家以為預言不靈了,因為拉辛格及
            德國同橄欖毫無瓜葛。然而, 當教廷宣佈新教宗選擇「本篤」作為自己的尊號時,人們才恍
            然大悟:歷史上的本篤修會,又被稱作為「橄欖修會」。 「教宗預言」指出,末代教宗名為
            羅馬人彼得(Peter the Roman,或譯為羅馬人伯多祿)。天主教會將在他治下走完最後的歷
            程。在「七山之城」毀滅後,世界末日將要到來,天主將會審判地上的子民。 這裡的羅馬,
            既可以指現代的義大利首都羅馬,更似指當年羅馬帝國的疆域。這似乎預示,新任教宗將來
            自於歐洲、北非或小亞細亞的環地中海地區。 來自非洲加納的黑人樞機、且被視為開明派
            的彼得.阿皮亞.圖克森(Peter Appiah Turkson),被問及非洲人當教宗的可能時說:「教會
            信眾遍全球,對天主教來說,非洲當然是一個重要的大洲,但同樣地亞洲也是......就奉行上
            帝的旨意。」
            '''
        ),
    )
    assert parsed_news.category == '國際要聞'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1362240000
    assert parsed_news.reporter is None
    assert parsed_news.title == '羅馬教廷神秘「手稿預言」與教宗退位風雲'
    assert parsed_news.url_pattern == '13-3-3-3813123'
