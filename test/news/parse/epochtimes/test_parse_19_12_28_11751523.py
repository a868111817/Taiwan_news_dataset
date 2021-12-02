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
    url = r'https://www.epochtimes.com/b5/19/12/28/n11751523.htm'
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
            大家經常聽到一句話「挾天子以令諸侯」,那麼奉迎天子到底給曹操帶來了什麼機遇和風險
            ? 西元196年對於漢獻帝,對於曹操都是非常重要的一年。這一年,曹操親自到洛陽迎接漢獻
            帝回到許昌,漢朝的首都正式遷到許昌。同樣就在這一年,漢朝更改年號,新的年號叫建安
            。 年號是中國古代用來紀年所起的一種名號。漢獻帝一共六個年號,第一個年號叫永漢,就是
            漢朝長長久久,永永遠遠的意思。非常有意思,漢朝最後就是終結在漢獻帝手裡,沒有永漢
            。 漢獻帝即位頭七年用了四個年號,而建安這個年號一用就用了二十五年。建安是什麼意思
            啊?建安建安,就是建立安寧,天下太平的意思。漢獻帝這一年只有十六歲,但是這前十六年
            過得太慘了,喪父喪母,哥哥被害,然後四處顛沛流離,被人追殺,被人綁架,有的時候吃不好,
            睡不好,住不好。更改新年號為建安就是希望天下太平,咱們以後別折騰了。 我們經常聽到
            這麼一句話「挾天子以令諸侯」,其實這句話不是曹操說的,是袁紹說的,準確地說,是袁紹的
            謀士說的。其實當時最有機會去奉迎天子的人不是曹操,而是袁紹。袁紹離漢獻帝近,手頭有
            錢、有兵、有糧。 當時袁紹的重要謀士沮授是這麼勸說袁紹的,「現在我們已經平定了
            很多地方,應當把皇上接過來,挾持天子來號令天下諸侯,養精蓄銳討伐不臣服的,誰能擋得了
            我們?」當然袁紹沒有聽這個建議,為什麼呢?其實是袁紹自己內心想要做皇帝,不想把漢獻帝
            接到身邊受制於人。袁紹不接漢獻帝,就把機會留給了曹操。 當時曹操的手下毛階就對曹操
            說,「我們要奉天子以令不臣。」奉天子和挾天子,一字之差,含義卻相差很大。袁紹挾天子
            那是把天子當成人質,而毛階的奉天子是把皇帝好好供養起來。曹操聽從了毛階的建議,在西元
            196年,親自帶兵去洛陽,迎接漢獻帝來到許昌,重新建立了朝廷。 任何時間事情都是風險和
            機遇並存的,奉迎天子就是一件機遇和風險並存的事情。那麼曹操奉迎天子以後到底給自己
            帶來了什麼優勢呢?又帶來了什麼風險呢? 奉迎天子帶來的第一個立竿見影的好處是人才
            歸順。曹操之前是州牧,就是省長,省長一般只能招自己省內的人,比如你河南省省長你去招
            一個江蘇的官員為你做官,江蘇省長可不答應。但是如果中央要徵調江蘇的人才去河南,那就
            順理成章,誰都攔不住,這是通俗的解釋。而學術的解釋是這樣的,漢朝有種用人制度叫徵辟,
            什麼是徵,就是皇帝看重了哪個人,下詔徵用他;什麼是辟,就是官府,比如宰相,看重誰就徵用
            誰。 所以曹操後來做了朝廷的司空,曹操招的很多人不是給朝廷招的,而是給自己司空府招
            的。司空是朝廷的宰相,你宰相要辦公處理公務,宰相府需要招人,怎麼招人,招什麼人,都是
            你司空自己說得算。所以曹操當時的很多人才都是曹操以司空名義招的,比如郭嘉,郭嘉的
            官職是什麼呢?司空軍祭酒。什麼意思?不是說郭嘉喝酒厲害,司空軍祭酒就是司空府的首席
            軍事參謀的意思,軍就是軍師,祭酒就是首席的意思。曹操不僅可以以司空的名義招人,
            在曹操奉迎天子之後還可以以皇帝的名義在全國範圍內徵辟人才了。 比如有個叫王朗的
            大臣,王朗當時是會稽太守,相當於現在杭州市長。王朗這個人治理地方很厲害,但是打仗
            不行,後來就被小霸王孫策打敗了。然後在孫策手下做官,一直留在江東。王朗名氣很大,
            是個人才,曹操早就聽說王朗的名聲,於是就表奏皇帝徵辟王朗來中央做官。這要放以前,曹操
            要是以兗州牧的身分徵召王朗,不僅孫策不會放,王朗自己可能也不會去。現在皇帝徵召你,
            孫策你可以不聽曹操的,但你總得給皇帝面子吧,所以孫策沒有辦法,就讓王朗走了。王朗來到
            曹操這,立了汗馬功勞,後來成為魏國建國以後的三公。 曹操還有個大臣叫華歆,和王朗簡直
            一模一樣,也是這麼來投奔曹操的。華歆當時也投降了孫策,華歆為官清廉,把地方也是治理得
            井井有條,很有才能,曹操當時也是用皇帝的名義徵召華歆回去做官。孫權(孫策已遇
            刺身亡)那個時候不想放,但是華歆想走,曹操又是用的皇帝詔書,朝廷要用人,你孫權不放
            也得放啊,你不放就是和朝廷對著幹。 得知華歆要離開孫權的消息時,有上千人為華歆送行,
            贈送給華歆的禮金多達幾百金,華歆當時沒有拒絕,但是暗中記下誰送了多少錢。等到華歆要
            上路的時候,就一一把禮金送還給每個人,說「我本來不想拒絕大家的心意,但是送給我的禮金
            太多了,我將要遠行,路上攜帶這麼多財寶要招致災禍的,請各位幫我個忙,把禮金拿回去吧。
            」華歆就這樣把禮金原封不動地還給了每個人。你看這麼一個為人為官都這麼好的人,曹操
            一封詔書就要來了。 到後來曹丕建立魏國的時候,有三個宰相(就是三公),一個是王朗,一個
            是華歆,剩下一個是賈詡。也就是說,魏國開國的宰相,有兩個人是曹操不花一分錢、不費
            一個兵,從孫策和孫權那裡要過來的。 不僅如此,也有很多人才聽到曹操奉迎天子主動來投靠
            曹操,比如曹操手底下有個叫趙儼的將領,因為戰亂躲到荊州去了,聽聞曹操奉迎天子,對
            自己的好朋友說,「曹操是承運天命,一定能夠匡濟天下,安定蒼生,現在是我回去的時候了。
            」然後趙儼帶著男女老少的族人啟程,不遠萬里去投奔曹操。這個趙儼歷史上不出名,但是在
            三國時期是很厲害的,赤壁之戰的時候,趙儼都督七軍,包括張遼、張郃、于禁等七支部隊
            。類似的事情還很多,比如郭嘉,比如荀攸,都是在這一時期投奔曹操的。 奉迎天子帶來的第
            二個效果就是諸侯投靠。第一個和曹操達成政治協定的是西北地方的割據勢力馬騰、韓遂。
            西元197年,馬騰和韓遂表示願意歸順朝廷,分別遣送兒子來許昌作為人質。這為曹操消除
            了西北方向的威脅,使得曹操能專心對付身邊的敵人。 第二個和曹操達成政治默契的不是
            別人,正是小霸王孫策。可能很多人不知道,曹操和孫策那可是親家,孫策的弟弟孫匡娶的老婆
            就是曹操的侄女。曹操的兒子曹彰娶的老婆是孫賁的女兒,孫賁是孫策的堂兄。 孫策
            為什麼要和曹操結親,有兩個原因:第一,曹操和孫策當時都有同樣的敵人,就是袁術。袁術在
            淮南稱帝,成為曹操和孫策進攻的對象。第二,當時孫策在江東立足未穩,急需朝廷給予自己
            封號來確立自己的正統性。所以西元197年,孫策被朝廷封為會稽太守,沿襲自己父親孫堅的
            爵位烏程侯。西元199年,曹操上表朝廷封孫策為漢朝討逆將軍,賜予吳侯的爵位
            。 第三個向曹操投靠的諸侯是張繡。關於張繡的事情比較複雜,我們今天要好好說說。張繡
            是我們之前說的張濟的侄子,這個張濟就是當時護送漢獻帝東歸的軍閥之一。後來張濟打仗被
            殺死了,張繡就帶領自己叔叔的軍隊,駐紮在宛城這個地方,投靠了荊州的劉表。西元197年,
            曹操南征張繡,張繡投降,可是投降沒過多久,張繡就背叛曹操。關於這次張繡背叛的原因,
            史書上給出兩種說法。 第一種是說張繡投降以後,曹操就娶了張繡的寡婦嫂子鄒夫人。
            張繡就很憤恨,曹操知道張繡對自己不滿,內心也懷疑起來,有了殺張繡的計畫。結果被張繡
            察覺,張繡偷襲曹操。 說到這裡我們講一個事情,就是在秦漢三國時期,寡婦嫁人是非常普遍
            的現象,為什麼呢?因為在中國古代,男子是家裡收入勞動的保證,沒了丈夫,生活就很有問題。
            我們舉個三國的例子,三國時期曹操手下有個謀士叫荀攸,荀攸死得早,荀攸的好朋友鐘繇就
            說了,「沒想到我的好朋友這麼年輕就病亡了,我現在要把你的妻子阿騖嫁出去,使她有個好
            歸宿。」可見在三國時期,好朋友病亡了,還要想辦法把好朋友的妻子嫁出去,所以曹操
            娶張繡的嫂子在那個時代是一個很普遍的做法。 關於張繡背叛的第二種說法,是說張繡
            手下有個大將叫胡車兒,勇冠三軍,曹操這個人特別愛惜人才,很喜歡胡車兒,就賞賜給胡車兒
            很多黃金。張繡懷疑曹操是想收買自己的手下來殺害自己,這才造反。 這兩種說法我們現在
            都無法斷定真假了,反正張繡當時是造反了,而曹操是一點準備都沒有。當時張繡表示要借道
            曹操的軍營行軍,張繡騙曹操說,「我們軍車少,但是輜重太多了,帶不了武器和戰甲,請允許
            我們士兵身披戰甲。」曹操就輕信了。 張繡的士兵全副武裝進入曹操的軍營,然後偷襲
            曹操。這場戰役打得是特別慘,曹操當時騎著一匹寶馬名叫絕影,被箭傷到臉和馬足,曹操的
            胳膊也被弓箭擊中,身受重傷。曹操的兒子曹昂將自己的馬讓給曹操,曹操才隻身逃脫,但是
            曹昂和曹操侄子曹安民都死在這裡。 曹操手下有個著名的勇士叫典韋,當時張繡投降以後
            雙方大宴賓客,大家都大口吃肉、大口喝酒,只有典韋手持大斧頭,一動不動站在曹操後面,
            曹操每到一個人跟前敬酒的時候,典韋就瞪著大眼,舉著斧頭盯著對方,張繡和他的部下沒有人
            敢看典韋。 張繡反叛的時候,典韋為了保護曹操,守衛在營門,在陣前殺敵無數,以一當十,
            典韋手持長戟左右看殺敵軍,一叉過去,就有十幾支矛被擊斷。他的手下死傷殆盡,典韋也身受
            幾十處傷,只得與敵人短兵相接。敵兵想上來活捉他,典韋用雙臂挾住兩個敵兵將他們殺死,
            其餘的兵賊不敢上前。典韋又衝上前去突擊敵人,殺死數人,這個時候典韋傷勢加重,雙目圓睜
            ,大罵而死。敵人這才敢上前去,割下他的頭,互相傳看。 曹操逃脫以後,知道這個消息,痛哭
            萬分,招募勇士偷偷把典韋的屍體偷回來,然後親自為典韋發喪,在葬禮上痛哭流涕。
            以後曹操每次經過典韋的墓地,都要親自用中牢的禮儀祭奠典韋。 曹操在宛城吃了打敗仗,
            後來和張繡僵持了好幾年。西元199年,當時曹操已經在前線和袁紹相持了,張繡卻投降了
            曹操,這又是怎麼一回事呢? 當時袁紹和曹操都想拉攏張繡,袁紹派遣使者要和張繡達成同盟
            ,張繡本來想要答應,張繡身邊一個重要謀士賈詡這個時候公然對使者說,「請你們回去謝絕
            袁將軍,你們將軍連兄弟都不能相容,怎麼能容納天下的人才呢?」張繡一聽,嚇傻了,「賈詡
            你怎麼這麼說話呢!」轉過頭去悄悄問賈詡,「哎呀,你看看你,這下我們怎麼辦啊。」賈詡
            說了,「不如我們投降曹操把。」張繡就不理解了,「現在袁紹強,而曹操弱,我們又和曹操有
            世仇,怎麼能投降曹操呢?」 賈詡說道,「這正是我們要歸順曹操的原因啊。曹操奉迎天子,
            號令天下,這是其一。袁紹強大,我們現在歸順了,只不過是錦上添花,人家不會看重我們。
            我們投降曹操,那是雪中送炭,曹操一定會看重我們的,這是第二個原因。曹操是有霸王志向
            的人,一定能冰釋前嫌,況且曹操以恩德享譽天下,這是第三個原因。將軍您不要猶豫了。」
            張繡一聽,覺得很有道理,就投降了曹操。 張繡投降的時候,曹操非常高興,還把自己的
            女兒許配給張繡的兒子,結為兒女親家。後來官渡之戰之後,曹操賞賜給張繡二千戶,這是個
            什麼概念?曹操著名的謀士賈詡位至三公,也不過才八百戶的封地,而大將軍夏侯惇也不過
            二千五百戶,張繡二千戶的封地其實非常高了。 奉迎天子這件事情帶給了曹操機遇,使得曹操
            能夠徵召天下的人才,而四方的諸侯也慢慢歸順,馬騰、韓遂排遣質子,孫策結為親家,而張繡
            也在西元199年投降曹操。可是奉迎天子這件事情啊既有機遇,也會有風險,那麼曹操到底從
            奉迎天子這件事情上又遇到了什麼危險呢? 「從之則權輕,違之則拒命」就是風險。曹操在
            奉迎了漢獻帝之後,一開始其實形勢並不樂觀,北方有強大的袁紹,東方有袁術和呂布,南邊有
            劉表和張繡,每一個人都居心叵測,在這樣的情況下,曹操是沒有辦法將權力給漢獻帝。漢獻帝
            從開始做皇帝起就沒有一天掌握過實權,可是這個時候的漢獻帝已經成年了,已經想要奪取權力
            ,這就和曹操產生了尖銳的衝突,也給曹操帶來了危機。西元200年初,發生了著名的衣帶詔
            事件。 這個事件在歷史上記載太過於簡單,以至於沒有什麼細節,《後漢書》是
            這麼說的,董承等人接受漢獻帝的秘密詔書要誅殺曹操,事情被暴露,董承等人被曹操所殺。而
            《三國志》的說法是,董承等人只是聲稱有皇帝詔書,這個詔書是不是真的皇帝寫得並不清楚
            。這個事情的具體過程我們已經不得而知了,我們可以確定的是,在曹操奉迎漢獻帝重新建立
            朝廷之後,漢獻帝在曹操腹背受敵的情況下,採取了暗殺曹操這樣一個行動。 這樣一個行動
            使得曹操和漢獻帝的關係完全破裂,但是面對想要置自己於死地的漢獻帝,曹操的態度是什麼
            呢?一個字,躲。曹操後來在平定北方之後幹的第一件事情就是把自己的都城許昌遷到鄴城,
            遠離漢獻帝。作為漢獻帝的臣子,你不可能殺了皇帝,但是待在一起又太危險了,那麼怎麼辦
            呢?只能躲開。 曹操從此之後,很少回到漢朝的都城許昌,每次出征,都是回到自己的封地鄴城
            ,比如赤壁之戰之後,潼關之戰之後,曹操都是回的鄴城,平時也都待在鄴城,減少和漢獻帝
            接觸的機會。 我們今天講,曹操奉迎漢獻帝,給自己帶來了機遇,也帶來了風險。曹操在這一
            階段把握了機遇,躲過了風險,逐鹿中原。就在這個時候,曹操收到了一封來信,曹操看了
            這封來信以後非常生氣,出入舉止都和平常非常不一樣,沒有人知道是為什麼,只有謀士荀彧
            看出來了曹操為什麼情緒變化這麼大,那麼到底是誰寫了封信讓曹操舉止這麼不平常呢?請看
            下集《亂世梟雄》。 沮授說紹曰:「將軍累葉輔弼,世濟忠義。今朝廷播越,宗廟毀壞,
            觀諸州郡外托義兵,內圖相滅,未有存主恤民者。且今州城粗定,宜迎大駕,安宮鄴都,挾天子
            而令諸侯,畜士馬以討不庭,誰能禦之!」 紹悅,將從之。郭圖、淳于瓊曰:「漢室陵遲,為日
            久矣,今欲興之,不亦難乎!且今英雄據有州郡,衆動萬計,所謂秦失其鹿,先得者王。若迎天子
            以自近,動輙表聞,從之則權輕,違之則拒命,非計之善者也。」 清·趙翼《陔余叢考·
            祭酒》祭酒本非官名,古時凡同輩之長,皆曰祭酒。 《三國志 華歆傳》太祖在官渡,表
            天子徵歆。孫權欲不遣,歆謂權曰:「將軍奉王命,始交好曹公,分義未固,使僕得為將軍效心,
            豈不有益乎?今空留僕,是為養無用之物,非將軍之良計也。」權悦,乃遣歆。賔客舊人送之者
            千餘人,贈遺數百金。歆皆無所拒,密各題識,至臨去,悉聚諸物,謂諸賔客曰:「本無拒諸君
            之心,而所受遂多。念單車遠行,將以懷璧為罪,願賔客為之計。」衆乃各留所贈,而服其德
            。 《三國志 趙儼傳》趙儼字伯然,潁川陽翟人也。避亂荊州,與杜襲、繁欽通財同計,
            合為一家。太祖始迎獻帝都許,儼謂欽曰:「曹鎮東應期命世,必能匡濟華夏,吾知歸矣。」
            建安二年,年二十七,遂扶持老弱詣太祖,太祖以儼為朗陵長。 《三國志 趙儼傳》太祖
            征荊州,以儼領章陵太守,徙都督護軍,護于禁、張遼、張郃、朱靈、李典、路招、馮楷七軍
            。 《三國志 鐘繇傳》時關中諸將馬騰、韓遂等,各擁強兵相與爭。太祖方有事山東,以
            關右為憂。乃表繇以侍中守司隷校尉,持節督關中諸軍,委之以後事,特使不拘科制。繇至長安
            ,移書騰、遂等,為陳禍福,騰、遂各遣子入侍。 《三國志 孫策傳》乃以弟女配策小弟
            匡,又為子章取賁女,皆禮辟策弟權、翊,又命揚州刺史嚴象舉權茂才。 曹公表策為討逆
            將軍,封為吳侯。 江表傳曰:建安三年,策又遣使貢方物,倍於元年所獻。其年,制書轉
            拜討逆將軍,改封吳侯。 《三國志 武帝紀》太祖納濟妻,繡恨之。太祖聞其不悅,
            密有殺繡之計。計漏,繡掩襲太祖。太祖軍敗,二子沒。 《三國志 方技傳》初,潁川
            荀攸、鍾繇相與親善。攸先亡,子幼。繇經紀其門戶,欲嫁其妾。與人書曰:「吾與公達曾共
            使朱建平相,建平曰:『荀君雖少,然當以後事付鍾君。』吾時啁之曰:『惟當嫁卿阿騖耳。』
            何意此子竟早隕沒,戲言遂驗乎!今欲嫁阿騖,使得善處。追思建平之妙,雖唐舉、許負何以
            複加也!」 《三國志 張繡傳》傅子曰:繡有所親胡車兒,勇冠其軍。太祖愛其驍健,
            手以金與之。繡聞而疑太祖欲因左右刺之,遂反。 吳書曰:繡降,用賈詡計,乞徙軍就
            高道,道由太祖屯中。繡又曰:「車少而重,乞得使兵各被甲。」太祖信繡,皆聽之。繡乃嚴兵
            入屯,掩太祖。太祖不備,故敗。 《三國志 典韋傳》時韋校尚有十餘人,皆殊死戰,
            無不一當十。賊前後至稍多,韋以長戟左右擊之,一叉入,輒十餘矛摧。左右死傷者略盡。韋
            複前突賊,殺數人,創重發,瞋目大罵而死。賊乃敢前,取其頭,傳觀之,覆軍就視其軀。太祖退
            住舞陰,聞韋死,為流涕,募閒取其喪,親自臨哭之,遣歸葬襄邑。 《三國志 賈詡傳
            》是後,太祖拒袁紹於官渡,紹遣人招繡,並與詡書結援。繡欲許之,詡顯於繡坐上謂紹使曰:
            「歸謝袁本初,兄弟不能相容,而能容天下國士乎?」繡驚懼曰:「何至於此!」竊謂詡曰:「
            若此,當何歸?」詡曰:「不如從曹公。」繡曰:「袁強曹弱,又與曹為讎,從之如何?」詡曰:
            「此乃所以宜從也。夫曹公奉天子以令天下,其宜從一也。紹強盛,我以少衆從之,必不以我
            為重。曹公衆弱,其得我必喜,其宜從二也。夫有霸王之志者,固將釋私怨,以明德於四海,其
            宜從三也。願將軍無疑!」繡從之,率衆歸太祖。太祖見之,喜,執詡手曰:「使我信重於天下
            者,子也。」 《三國志 武帝紀》董承等謀洩,皆伏誅。 《後漢書 獻帝紀》
            五年春正月,車騎將軍董承、偏將軍王服、越騎校尉種輯受密詔誅曹操,事洩。壬午,曹操殺
            董承等,夷三族。 《三國志 荀彧傳》紹益驕,與太祖書,其辭悖慢。太祖大怒,出入
            動靜變於常,衆皆謂以失利於張繡故也。
            '''
        ),
    )
    assert parsed_news.category == '文化網,史海鉤沉,中國歷代名人,傳奇人物'
    assert parsed_news.company_id == company_id
    assert parsed_news.timestamp == 1577462400
    assert parsed_news.reporter is None
    assert parsed_news.title == '奉天子帶來的機遇和風險'
    assert parsed_news.url_pattern == '19-12-28-11751523'
