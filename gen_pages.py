# -*- coding: utf-8 -*-
import os, io, re

BASE = r"C:\Users\VT86\Documents\Codex\2026-08-18\c\outputs\voyager-clone"

NAV_CN = [("index.html","首页"),("about.html","关于寅家"),("tech.html","技术路线"),("news.html","企业动态"),("honors.html","企业荣誉"),("contact.html","联系我们")]
NAV_TW = [("../index.html","首頁"),("about.html","關於寅家"),("tech.html","技術路線"),("news.html","企業動態"),("honors.html","企業榮譽"),("contact.html","聯絡我們")]
NAV_EN = [("../index.html","Home"),("about.html","About"),("tech.html","Technology"),("news.html","News"),("honors.html","Recognition"),("contact.html","Contact")]

def header(lang, nav, active, pre, title, desc):
    if lang == "cn":
        lang_switch = '<a href="index.html" class="on">简</a><a href="zh-Hant/index.html">繁</a><a href="en/index.html">EN</a>'
    elif lang == "tw":
        lang_switch = '<a href="../index.html">简</a><a href="index.html" class="on">繁</a><a href="../en/index.html">EN</a>'
    else:
        lang_switch = '<a href="../index.html">简</a><a href="../zh-Hant/index.html">繁</a><a href="index.html" class="on">EN</a>'
    nav_html = "".join('<a href="%s"%s>%s</a>' % (h, ' class="active"' if h == active else "", t) for h, t in nav)
    return """<!DOCTYPE html>
<html lang="%s">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="stylesheet" href="%sassets/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="%s">
      <img class="logo-img" src="%sassets/img/logo-header.png" alt="VOYISL">
    </a>
    <nav class="nav" id="mainNav">
      %s
      <div class="lang-switch">%s</div>
    </nav>
    <button class="menu-btn" aria-label="Menu">&#9776;</button>
  </div>
</header>
""" % (lang, title, desc, pre, pre + "index.html", pre, nav_html, lang_switch)

def hero(title, en):
    return """<section class="page-hero">
  <div class="bg"></div>
  <div class="inner">
    <p class="en">%s</p>
    <h1>%s</h1>
    <span class="bar"></span>
  </div>
</section>""" % (en, title)

def footer(pre, lang, home_href):
    if lang == "cn":
        brand = "寅家科技"; qr = "扫描二维码，关注寅家科技官方公众号"
        navt = "快速导航"; links_t = "友情链接"
        qt = [("about.html","关于寅家"),("tech.html","技术路线"),("news.html","企业动态"),("honors.html","企业荣誉"),("contact.html","联系我们")]
        fl = [("http://www.yu-zhou.com/","上海宇宙电器"),("http://wuhuruishida.com/","瑞视达光学"),("#","梅克朗寅家")]
    elif lang == "tw":
        brand = "寅家科技"; qr = "掃描二維碼，關注寅家科技官方公眾號"
        navt = "快速導覽"; links_t = "友情連結"
        qt = [("about.html","關於寅家"),("tech.html","技術路線"),("news.html","企業動態"),("honors.html","企業榮譽"),("contact.html","聯絡我們")]
        fl = [("http://www.yu-zhou.com/","上海宇宙電器"),("http://wuhuruishida.com/","瑞視達光學"),("#","梅克朗寅家")]
    else:
        brand = "VOYISL"; qr = "Scan the QR code to follow our official account"
        navt = "Quick Links"; links_t = "Related Links"
        qt = [("about.html","About"),("tech.html","Technology"),("news.html","News"),("honors.html","Recognition"),("contact.html","Contact")]
        fl = [("http://www.yu-zhou.com/","Shanghai Yu-Zhou Electric"),("http://wuhuruishida.com/","Wuhu Ruishida Optics"),("#","MEKRA Lang VOYISL")]
    q = "".join('<a href="%s">%s</a>' % (h, t) for h, t in qt)
    fl_html = "".join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (h, t) for h, t in fl)
    return """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h5>%s</h5>
        <p>%s</p>
        <img class="footer-qr" src="%sassets/img/qr-wechat.jpg" alt="QR">
      </div>
      <div>
        <h5>%s</h5>
        %s
      </div>
      <div>
        <h5>%s</h5>
        %s
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 寅家科技 VOYISL</span>
      <span><a href="%s">简体中文</a> | <a href="%szh-Hant/index.html">繁體中文</a> | <a href="%sen/index.html">English</a></span>
    </div>
  </div>
</footer>
<script src="%sassets/js/main.js"></script>
</body>
</html>""" % (brand, qr, pre, navt, q, links_t, fl_html, home_href, pre, pre, pre)

def build_page(lang, nav, active, pre, title, desc, hero_title, content):
    home_href = pre + "index.html"
    return header(lang, nav, active, pre, title, desc) + hero(hero_title, desc) + content + footer(pre, lang, home_href)

def write(fname, html, langdir):
    d = os.path.join(BASE, langdir)
    os.makedirs(d, exist_ok=True)
    with io.open(os.path.join(d, fname), "w", encoding="utf-8") as f:
        html = re.sub(r'<p class="en">([^<]+)</p>(\s*)<h2([^>]*)>\1</h2>', r'<h2\3>\1</h2>', html)  # dedup eyebrow==h2
    f.write(html)

def content_about(lang, pre):
    if lang == "cn":
        cards = [("品牌使命","以自研科技，赋能全球智慧出行"),("品牌愿景","致力于成为跨领域智能应用先行者"),("品牌格局","在中国，为世界")]
        tl = [("初心元年","海归技术团队创业，较早一批国产智能辅助驾驶产品创业公司；确立基于视觉感知的软硬一体化产品战略；国内较早进行BEV架构应用。"),
              ("产品问世","3D全景环视产品发布；APA自动泊车辅助和AVP代客泊车系统发布；成为丰田-雷克萨斯视觉感知产品国产合作伙伴。"),
              ("量产突破","智能辅助驾驶系统出货量突破10万套；认证上海市高新技术企业；平台化产品VT-Pilot®具备雏形。"),
              ("走出国门","实现智能辅助驾驶系统出口目标；量产产品覆盖车型超一百款；嘉兴、芜湖智能生产基地落成。"),
              ("蓄力爆发","加速VT-Cockpit®座舱产品布局；VT-Vulcan®域控系列发布；与梅克朗集团中国子公司合资；业务拓展至欧洲、南/北美、东南亚、日韩。"),
              ("载誉前行","国家高新技术企业认定；教育部科学研究优秀成果奖二等奖；2026福布斯中国行业发展领创者；2026中国出行科技全球化新锐品牌TOP10。")]
        p1 = "寅家科技创立于2013年，依托全栈自研的核心技术，实现智能感知、智能决策与控制技术在多领域通用智能体的规模化应用。"
        p2 = "深耕汽车产业十余年，公司持续加码人工智能技术研发，将地面出行智能技术体系延伸赋能低空经济、具身机器人等新兴赛道，积极布局全球市场。"
        h2 = "关于寅家"
    elif lang == "tw":
        cards = [("品牌使命","以自研科技，賦能全球智慧出行"),("品牌願景","致力於成為跨領域智能應用先行者"),("品牌格局","在中國，為世界")]
        tl = [("初心元年","海歸技術團隊創業，較早一批國產智能輔助駕駛產品創業公司；確立基於視覺感知的軟硬一體化產品戰略；國內較早進行BEV架構應用。"),
              ("產品問世","3D全景環視產品發佈；APA自動泊車輔助和AVP代客泊車系統發佈；成為豐田-雷克薩斯視覺感知產品國產合作夥伴。"),
              ("量產突破","智能輔助駕駛系統出貨量突破10萬套；認證上海市高新技術企業；平台化產品VT-Pilot®具備雛形。"),
              ("走出國門","實現智能輔助駕駛系統出口目標；量產產品覆蓋車型超一百款；嘉興、蕪湖智能生產基地落成。"),
              ("蓄力爆發","加速VT-Cockpit®座艙產品佈局；VT-Vulcan®域控系列發佈；與梅克朗集團中國子公司合資；業務拓展至歐洲、南/北美、東南亞、日韓。"),
              ("載譽前行","國家高新技術企業認定；教育部科學研究優秀成果獎二等獎；2026福布斯中國行業發展領創者；2026中國出行科技全球化新銳品牌TOP10。")]
        p1 = "寅家科技創立於2013年，依託全棧自研的核心技術，實現智能感知、智能決策與控制技術在多領域通用智能體的規模化應用。"
        p2 = "深耕汽車產業十餘年，公司持續加碼人工智能技術研發，將地面出行智能技術體系延伸賦能低空經濟、具身機器人等新興賽道，積極佈局全球市場。"
        h2 = "關於寅家"
    else:
        cards = [("Mission","Empowering global smart mobility with self-developed technology"),("Vision","Becoming a leading cross-domain intelligent application pioneer"),("Positioning","In China, for the world")]
        tl = [("The Beginning","Founded by a returnee technical team, among the first domestic startups in intelligent driving; established a software-hardware integrated strategy based on visual perception."),
              ("Product Launch","Released 3D surround-view, APA automated parking assist and AVP valet parking systems; became a domestic partner for Toyota-Lexus visual perception products."),
              ("Mass Production","Intelligent driving system shipments exceeded 100,000 sets; certified as a Shanghai High-Tech Enterprise; formed the VT-Pilot® platform."),
              ("Going Global","Achieved export targets; mass-production products covered over 100 vehicle models; established Jiaxing and Wuhu smart manufacturing bases."),
              ("Expansion","Accelerated VT-Cockpit® cabin products; launched VT-Vulcan® domain controllers; joint venture with MEKRA Lang China; expanded to Europe, Americas, Southeast Asia, Japan and Korea."),
              ("Recognition","Certified National High-Tech Enterprise; awarded by the Ministry of Education; named a 2026 Forbes China industry pioneer and a GoGlobal TOP10 brand.")]
        p1 = "Founded in 2013, VOYISL delivers large-scale applications of intelligent perception, decision and control technologies across multiple domains through its full-stack self-developed core technologies."
        p2 = "With over a decade in the automotive industry, the company keeps investing in AI R&D, extending ground mobility intelligence to low-altitude economy and embodied robotics while expanding into global markets."
        h2 = "About VOYISL"
    c = "".join('<div class="mvv reveal"><span class="tag">%s</span><h4>%s</h4><p>%s</p></div>' % (t, t, d) for t, d in cards)
    t = "".join('<div class="tl-item reveal"><div class="year">0%d</div><h4>%s</h4><p>%s</p></div>' % (i+1, x[0], x[1]) for i, x in enumerate(tl))
    return """<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal"><p class="en">About VOYISL</p><h2>%s</h2><span class="bar"></span></div>
    <div class="about-grid">
      <div class="reveal">
        <h3>%s</h3>
        <p>%s</p>
        <p>%s</p>
      </div>
      <div class="about-visual reveal"><img src="%sassets/img/about.jpg" alt="about"></div>
    </div>
    <div class="mvv-grid" style="margin-top:56px">%s</div>
    <div class="sec-head reveal" style="margin-top:72px"><p class="en">Milestones</p><h2>%s</h2><span class="bar"></span></div>
    <div class="timeline">%s</div>
  </div>
</section>""" % (h2, cards[0][1], p1, p2, pre, c, ("發展歷程" if lang == "tw" else ("发展历程" if lang == "cn" else "Milestones")), t)

def content_tech(lang, pre):
    if lang == "cn":
        intro = "以智能感知、智能决策与控制技术，赋能多领域通用智能体规模化应用"
        s1 = ("智能感知","VT-Sensing / VT-Navi","多目摄像头与深度学习算法，实现目标识别、车道线检测、盲区监测与全景环视。")
        s2 = ("融合定位","VT-Navi","融合视觉、惯导、轮速等多源信息，构建高精度定位与建图能力。")
        s3 = ("决策控制","VT-Vulcan®","基于域控平台与车规级安全架构，统筹规划、决策与执行。")
        cams = [("RVC摄像头","1M-2M"),("AVM/APA摄像头","1M-3M"),("FVC前视一体机","8M"),("SVC/CMS摄像头","2M-3M/3M"),("DMS摄像头","2M-3M"),("OMS摄像头","5M")]
        h2, h2c = "技术路线", "智能感知产品线"
    elif lang == "tw":
        intro = "以智能感知、智能決策與控制技術，賦能多領域通用智能體規模化應用"
        s1 = ("智能感知","VT-Sensing / VT-Navi","多目相機與深度學習演算法，實現目標識別、車道線檢測、盲區監測與全景環視。")
        s2 = ("融合定位","VT-Navi","融合視覺、慣導、輪速等多源資訊，構建高精度定位與建圖能力。")
        s3 = ("決策控制","VT-Vulcan®","基於域控平台與車規級安全架構，統籌規劃、決策與執行。")
        cams = [("RVC攝像頭","1M-2M"),("AVM/APA攝像頭","1M-3M"),("FVC前視一體機","8M"),("SVC/CMS攝像頭","2M-3M/3M"),("DMS攝像頭","2M-3M"),("OMS攝像頭","5M")]
        h2, h2c = "技術路線", "智能感知產品線"
    else:
        intro = "Empowering large-scale application of general intelligent agents with perception, decision and control technologies"
        s1 = ("Visual Perception","VT-Sensing / VT-Navi","Multi-camera perception with deep learning for object detection, lane marking, blind-spot monitoring and surround view.")
        s2 = ("Fusion Positioning","VT-Navi","Fusing vision, inertial and wheel-speed data for high-accuracy localization and mapping.")
        s3 = ("Decision Control","VT-Vulcan®","Domain controller platform with automotive-grade safety architecture for planning, decision and execution.")
        cams = [("RVC Camera","1M-2M"),("AVM/APA Camera","1M-3M"),("FVC Front Camera","8M"),("SVC/CMS Camera","2M-3M/3M"),("DMS Camera","2M-3M"),("OMS Camera","5M")]
        h2, h2c = "Technology Roadmap", "Camera Lineup"
    cards = [
        '<article class="tech-card reveal"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><circle cx="12" cy="12" r="3.2"/><path d="M12 2.8v2.4M12 18.8v2.4M2.8 12h2.4M18.8 12h2.4M5.6 5.6l1.7 1.7M16.7 16.7l1.7 1.7M18.4 5.6l-1.7 1.7M7.3 16.7l-1.7 1.7"/></svg></div><h4>%s</h4><span class="en">%s</span><p>%s</p></article>' % (s1[0], s1[1], s1[2]),
        '<article class="tech-card reveal"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 21s-7-6.2-7-11a7 7 0 1 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/></svg></div><h4>%s</h4><span class="en">%s</span><p>%s</p></article>' % (s2[0], s2[1], s2[2]),
        '<article class="tech-card reveal"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 2 4 6v6c0 4.4 3.4 8.2 8 10 4.6-1.8 8-5.6 8-10V6z"/><path d="m9 12 2 2 4-4.5"/></svg></div><h4>%s</h4><span class="en">%s</span><p>%s</p></article>' % (s3[0], s3[1], s3[2]),
    ]
    cam_html = "".join('<div class="cam reveal"><b>%s</b><span>%s</span></div>' % (n, r) for n, r in cams)
    return """<section class="sec" style="background:#fff">
  <div class="wrap">
    <div class="sec-head reveal"><p class="en">Technology Roadmap</p><h2>%s</h2><span class="bar"></span></div>
    <p class="reveal" style="text-align:center;color:var(--muted);max-width:760px;margin:0 auto 44px">%s</p>
    <div class="tech-grid">%s</div>
    <div class="sec-head reveal" style="margin-top:72px"><p class="en">Camera Lineup</p><h2>%s</h2><span class="bar"></span></div>
    <div class="cam-grid">%s</div>
  </div>
</section>""" % (h2, intro, "".join(cards), h2c, cam_html)

def content_news(lang, pre):
    if lang == "cn":
        items = [("07","2026","聚力巴西，深化南美布局 | 寅家科技携手梅克朗、Metagal 亮相梅赛德斯-奔驰技术日","深化海外布局，携手产业链伙伴共同拓展南美及欧洲市场。"),
                 ("06","2026","GB 47955新规来袭，寅家靠“眼·脑·身”拿下L2安全考题","以“眼·脑·身”技术框架响应新规要求，保障 L2 安全。"),
                 ("05","2026","寅家WAIC时刻 | 亮出“眼·脑·身”物理AI量产解决方案","亮相世界人工智能大会 WAIC，展示量产级物理 AI 解决方案。"),
                 ("05","2026","Meet AI, Meet VOYISL | 寅家集团邀您参加 WAIC 2026","与全球伙伴共赴 AI 盛会，见证智能出行新未来。"),
                 ("04","2026","第一财经专访 | 对话寅家科技CEO陈寅仁","从技术验证走向规模量产，畅谈智能驾驶行业趋势。"),
                 ("03","2026","寅家科技荣获【2026中国出行科技全球化新锐品牌TOP10】","凭借量产能力与海外交付表现荣登年度新锐品牌榜单。")]
        h2 = "企业动态"
    elif lang == "tw":
        items = [("07","2026","聚力巴西，深化南美佈局 | 寅家科技攜手梅克朗、Metagal 亮相梅賽德斯-賓士技術日","深化海外佈局，攜手產業鏈夥伴共同拓展南美及歐洲市場。"),
                 ("06","2026","GB 47955新規來襲，寅家靠「眼·腦·身」拿下L2安全考題","以「眼·腦·身」技術框架響應新規要求，保障 L2 安全。"),
                 ("05","2026","寅家WAIC時刻 | 亮出「眼·腦·身」物理AI量產解決方案","亮相世界人工智慧大會 WAIC，展示量產級物理 AI 解決方案。"),
                 ("05","2026","Meet AI, Meet VOYISL | 寅家集團邀您參加 WAIC 2026","與全球夥伴共赴 AI 盛會，見證智慧出行新未來。"),
                 ("04","2026","第一財經專訪 | 對話寅家科技CEO陳寅仁","從技術驗證走向規模量產，暢談智慧駕駛行業趨勢。"),
                 ("03","2026","寅家科技榮獲【2026中國出行科技全球化新銳品牌TOP10】","憑藉量產能力與海外交付表現榮登年度新銳品牌榜單。")]
        h2 = "企業動態"
    else:
        items = [("07","2026","Gathering Strength in Brazil: VOYISL Partners with MEKRA Lang and Metagal at Mercedes-Benz Tech Day","Deepening our overseas footprint together with industry partners across South America and Europe."),
                 ("06","2026","GB 47955 Takes Effect: Meeting L2 Safety Standards with the \"Eye-Brain-Body\" Framework","Responding to the new regulation with our full-stack framework to secure L2 safety."),
                 ("05","2026","VOYISL at WAIC: Unveiling Mass-Production Physical AI Solutions","Showcasing production-grade physical AI solutions at the World AI Conference."),
                 ("05","2026","Meet AI, Meet VOYISL: Join Us at WAIC 2026","Join global partners at the AI summit and experience the future of smart mobility."),
                 ("04","2026","Yicai Exclusive Interview: Dialogue with Brian Chen, CEO of VOYISL","From technology validation to scale production — insights into intelligent driving trends."),
                 ("03","2026","VOYISL Named Among 2026 China GoGlobal Emerging Mobility Technology Brands TOP10","Recognized for mass-production capability and overseas delivery performance.")]
        h2 = "News Center"
    imgs = ["news-1.jpg","news-2.jpg","news-3.png","news-4.png","news-5.png","news-6.png"]
    n = "".join('<article class="news-item reveal"><img class="news-img" src="%sassets/img/%s" alt="news"><div class="date"><b>%s</b><span>%s</span></div><div><h4>%s</h4><p>%s</p></div></article>' % (pre, img, a, b, t, d) for (a,b,t,d), img in zip(items, imgs))
    return """<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal"><p class="en">News Center</p><h2>%s</h2><span class="bar"></span></div>
    <div class="news-list">%s</div>
  </div>
</section>""" % (h2, n)

def content_honors(lang, pre):
    if lang == "cn":
        items = [("2026福布斯中国行业发展领创者","寅家科技CEO陈寅仁"),("教育部科学研究优秀成果奖","工程技术研究成果奖二等奖"),("2026中国出行科技全球化新锐品牌TOP10","出海全球化智库EqualOcean"),("2026全球汽车供应链技术创新生态伙伴奖","《中国汽车报》")]
        h2 = "企业荣誉"
    elif lang == "tw":
        items = [("2026福布斯中國行業發展領創者","寅家科技CEO陳寅仁"),("教育部科學研究優秀成果獎","工程技術研究成果獎二等獎"),("2026中國出行科技全球化新銳品牌TOP10","出海全球化智庫EqualOcean"),("2026全球汽車供應鏈技術創新生態夥伴獎","《中國汽車報》")]
        h2 = "企業榮譽"
    else:
        items = [("2026 Forbes China Industry Development Pioneer","Brian Chen, CEO of VOYISL"),("Ministry of Education Outstanding Scientific Research Achievement Award","Second Prize in Engineering Technology Research Achievement"),("2026 China GoGlobal Emerging Mobility Technology Brand TOP10","EqualOcean GoGlobal Think Tank"),("2026 Global Automotive Supply Chain Technology Innovation Ecosystem Partner Award","China Automotive News")]
        h2 = "Recognition"
    cards = "".join('<div class="honor reveal"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.5"><circle cx="12" cy="9" r="5.4"/><path d="M8.6 13.6 7 21l5-2.6L17 21l-1.6-7.4"/></svg><b>%s</b><span>%s</span></div>' % (t, d) for t, d in items)
    return """<section class="sec honors">
  <div class="wrap">
    <div class="sec-head reveal"><p class="en">HONORS</p><h2>%s</h2><span class="bar"></span></div>
    <div class="honor-grid">%s</div>
  </div>
</section>""" % (h2, cards)

def content_contact(lang, pre):
    if lang == "cn":
        h3 = "商务咨询，请联系 <br>sales@voyager-tech.com"
        addr = "上海市闵行区顾戴路2337号维璟中心G栋"
        note = "* 演示站点表单，提交不会发送真实数据"; done = "提交成功"
        ph = ("请输入姓名","请输入公司/职位","请输入手机号码","请输入咨询内容")
        h2 = "联系我们"
    elif lang == "tw":
        h3 = "商務諮詢，請聯繫 <br>sales@voyager-tech.com"
        addr = "上海市閔行區顧戴路2337號維璟中心G棟"
        note = "* 演示站點表單，提交不會發送真實數據"; done = "提交成功"
        ph = ("請輸入姓名","請輸入公司/職位","請輸入手機號碼","請輸入諮詢內容")
        h2 = "聯絡我們"
    else:
        h3 = "For business consultation, please contact <br>sales@voyager-tech.com"
        addr = "Building G, Weijing Center, 2337 Guda Road, Minhang District, Shanghai"
        note = "* Demo site form; no real data is sent"; done = "Submitted"
        ph = ("Enter your name","Company / position","Enter your phone number","Enter your inquiry")
        h2 = "Contact Us"
    loc = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 21s-7-6.2-7-11a7 7 0 1 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>'
    mail = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M4 6h16v12H4z"/><path d="m4 7 8 6 8-6"/></svg>'
    return """<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal"><p class="en">Contact Us</p><h2>%s</h2><span class="bar"></span></div>
    <div class="contact-grid">
      <div class="contact-info reveal">
        <h3>%s</h3>
        <div class="row">%s<span>%s</span></div>
        <div class="row">%s<span>sales@voyager-tech.com</span></div>
      </div>
      <form class="form-card reveal" id="contactForm">
        <div class="form-grid">
          <div><label for="fName">%s</label><input id="fName" name="name" type="text" placeholder="%s" required></div>
          <div><label for="fCompany">%s</label><input id="fCompany" name="company" type="text" placeholder="%s"></div>
          <div class="full"><label for="fPhone">%s</label><input id="fPhone" name="phone" type="tel" placeholder="%s" required></div>
          <div class="full"><label for="fMsg">%s</label><textarea id="fMsg" name="message" placeholder="%s"></textarea></div>
        </div>
        <div class="submit-row">
          <button class="btn" type="submit" data-done="%s">%s</button>
          <span class="form-note">%s</span>
        </div>
      </form>
    </div>
  </div>
</section>""" % (h2, h3, loc, addr, mail, "姓名 *" if lang != "en" else "Name *", ph[0], "公司 / 职位" if lang != "en" else "Company / Position", ph[1], "手机号 *" if lang != "en" else "Phone *", ph[2], "备注 / 咨询内容" if lang != "en" else "Message", ph[3], done, "提交" if lang != "en" else "Submit", note)

def make_title(lang, name):
    return ("寅家科技 VOYISL - " + name) if lang != "en" else ("VOYISL - " + name)

CONFIGS = [
    ("cn", "", NAV_CN),
    ("tw", "zh-Hant/", NAV_TW),
    ("en", "en/", NAV_EN),
]
HERO = {
    "cn": {"about.html":"关于寅家","tech.html":"技术路线","news.html":"企业动态","honors.html":"企业荣誉","contact.html":"联系我们"},
    "tw": {"about.html":"關於寅家","tech.html":"技術路線","news.html":"企業動態","honors.html":"企業榮譽","contact.html":"聯絡我們"},
    "en": {"about.html":"About VOYISL","tech.html":"Technology Roadmap","news.html":"News Center","honors.html":"Recognition","contact.html":"Contact Us"},
}
PAGES = [
    ("about.html", "about", "About VOYISL", content_about),
    ("tech.html", "tech", "Technology Roadmap", content_tech),
    ("news.html", "news", "News Center", content_news),
    ("honors.html", "honors", "HONORS", content_honors),
    ("contact.html", "contact", "Contact Us", content_contact),
]
for lang, ldir, nav in CONFIGS:
    pre = "../" if lang in ("tw", "en") else ""
    for fname, key, en, fn in PAGES:
        name = {"cn": HERO["cn"][fname], "tw": HERO["tw"][fname], "en": HERO["en"][fname]}[lang]
        content = fn(lang, pre)
        html = build_page(lang, nav, active=fname, pre=pre, title=make_title(lang, name), desc=en, hero_title=name, content=content)
        write(fname, html, ldir)
        print("wrote", ldir + fname)
print("DONE")
