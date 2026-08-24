# -*- coding: utf-8 -*-
# Generate join.html (Join Us / careers) in 3 languages.
import os, io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = r"C:\Users\VT86\Documents\Codex\2026-08-18\c\outputs\voyager-clone"

def header(lang, pre, title, desc):
    if lang == "cn":
        nav = ('<a href="index.html">首页</a>\n      <a href="about.html">关于寅家</a>\n      <a href="tech.html">技术路线</a>'
               '<span class="has-drop"><a href="agents.html">通用智能体</a><span class="drop">'
               '<a href="agents-car.html">智能汽车</a><a href="agents-agri.html">农业机器人</a>'
               '<a href="agents-lowalt.html">低空经济</a><a href="agents-robot.html">具身机器人</a></span></span>\n      '
               '<a href="news.html">企业动态</a>\n      <a href="join.html" class="active">加入我们</a>')
        lang_switch = '<a href="index.html" class="on">简</a>\n        <a href="zh-Hant/index.html">繁</a>\n        <a href="en/index.html">EN</a>'
        menu = "菜单"; html_lang = "zh-CN"
    elif lang == "tw":
        nav = ('<a href="../index.html">首頁</a>\n      <a href="about.html">關於寅家</a>\n      <a href="tech.html">技術路線</a>'
               '<span class="has-drop"><a href="agents.html">通用智能體</a><span class="drop">'
               '<a href="agents-car.html">智能汽車</a><a href="agents-agri.html">農業機器人</a>'
               '<a href="agents-lowalt.html">低空經濟</a><a href="agents-robot.html">具身機器人</a></span></span>\n      '
               '<a href="news.html">企業動態</a>\n      <a href="join.html" class="active">加入我們</a>')
        lang_switch = '<a href="../index.html">簡</a>\n        <a href="index.html" class="on">繁</a>\n        <a href="../en/index.html">EN</a>'
        menu = "選單"; html_lang = "zh-Hant"
    else:
        nav = ('<a href="../index.html">Home</a>\n      <a href="about.html">About</a>\n      <a href="tech.html">Technology</a>'
               '<span class="has-drop"><a href="agents.html">Agents</a><span class="drop">'
               '<a href="agents-car.html">Intelligent Vehicle</a><a href="agents-agri.html">Agricultural Robot</a>'
               '<a href="agents-lowalt.html">Low-Altitude Economy</a><a href="agents-robot.html">Embodied Robot</a></span></span>\n      '
               '<a href="news.html">News</a>\n      <a href="join.html" class="active">Join Us</a>')
        lang_switch = '<a href="../index.html">简</a>\n        <a href="../zh-Hant/index.html">繁</a>\n        <a href="index.html" class="on">EN</a>'
        menu = "Menu"; html_lang = "en"
    return """<!DOCTYPE html>
<html lang="%s">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>寅家科技 VOYISL - %s</title>
<meta name="description" content="%s">
<link rel="stylesheet" href="%sassets/css/style.css?v=7">
</head>
<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="%sindex.html">
      <img class="logo-img" src="%sassets/img/logo-header.png" alt="VOYISL">
    </a>
    <nav class="nav" id="mainNav">
      %s
      <div class="lang-switch">
        %s
      </div>
    </nav>
    <button class="menu-btn" aria-label="%s">&#9776;</button>
  </div>
</header>
""" % (html_lang, title, desc, pre, pre, pre, nav, lang_switch, menu)

def footer(lang, pre):
    if lang == "cn":
        brand = "寅家科技"; qr = "扫描二维码，关注寅家科技官方公众号"; navt = "快速导航"; linkt = "友情链接"
        qt = [("about.html","关于寅家"),("tech.html","技术路线"),("agents.html","通用智能体"),("news.html","企业动态"),("honors.html","企业荣誉"),("join.html","加入我们")]
        fl = [("http://www.yu-zhou.com/","上海宇宙电器"),("http://wuhuruishida.com/","瑞视达光学")]
        copy = "© 2026 寅家科技 VOYISL（演示复刻站点）"
        langs = "简体中文 | " + '<a href="zh-Hant/index.html">繁體中文</a> | <a href="en/index.html">English</a>'
    elif lang == "tw":
        brand = "寅家科技"; qr = "掃描二維碼，關注寅家科技官方公眾號"; navt = "快速導覽"; linkt = "友情連結"
        qt = [("about.html","關於寅家"),("tech.html","技術路線"),("agents.html","通用智能體"),("news.html","企業動態"),("honors.html","企業榮譽"),("join.html","加入我們")]
        fl = [("http://www.yu-zhou.com/","上海宇宙電器"),("http://wuhuruishida.com/","瑞視達光學")]
        copy = "© 2026 寅家科技 VOYISL（演示復刻站點）"
        langs = '<a href="../index.html">简体中文</a> | 繁體中文 | <a href="../en/index.html">English</a>'
    else:
        brand = "VOYISL"; qr = "Scan the QR code to follow our official account"; navt = "Quick Links"; linkt = "Related Links"
        qt = [("about.html","About"),("tech.html","Technology"),("agents.html","Agents"),("news.html","News"),("honors.html","Recognition"),("join.html","Join Us")]
        fl = [("http://www.yu-zhou.com/","Shanghai Yu-Zhou Electric"),("http://wuhuruishida.com/","Wuhu Ruishida Optics")]
        copy = "© 2026 VOYISL (Demo replica site)"
        langs = '<a href="../index.html">简体中文</a> | <a href="../zh-Hant/index.html">繁體中文</a> | English'
    q = "".join('<a href="%s">%s</a>' % (h, t) for h, t in qt)
    f = "".join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (h, t) for h, t in fl)
    return """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h5>%s</h5>
        <p style="margin-top:12px">%s</p>
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
      <span>%s</span>
      <span>%s</span>
    </div>
  </div>
</footer>
<script src="%sassets/js/main.js"></script>
</body>
</html>
""" % (brand, qr, pre, navt, q, linkt, f, copy, langs, pre)

ICO_STAR = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.5"><path d="M12 2l2.9 6.3 6.9.8-5.1 4.7 1.4 6.8L12 17.2 5.9 20.6l1.4-6.8L2.2 9.1l6.9-.8z"/></svg>'
ICO_GROW = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.5"><path d="M3 20h18"/><path d="M6 20V10m6 10V4m6 16v-8"/></svg>'
ICO_GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.5"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.7 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.7-3.8-9S9.5 5.5 12 3z"/></svg>'
ICO_HEART = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.5"><path d="M12 21s-8-5.3-8-11a4.6 4.6 0 0 1 8-3 4.6 4.6 0 0 1 8 3c0 5.7-8 11-8 11z"/></svg>'
ICO_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 21s-7-6.2-7-11a7 7 0 1 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>'

def body(lang, pre, d):
    whys = ""
    icos = [ICO_STAR, ICO_GROW, ICO_GLOBE, ICO_HEART]
    for i, (t, p) in enumerate(d["why"]):
        whys += '<div class="agent reveal"><div class="ico">%s</div><h4>%s</h4><p>%s</p></div>\n      ' % (icos[i], t, p)
    chips = "".join("<span>%s</span>" % c for c in d["culture"])
    cities = "".join('<div class="stat-card"><div class="num">%s</div></div>' % c for c in d["cities"])
    banner = ""
    if os.path.exists(os.path.join(BASE, "assets", "img", "join-banner.jpg")):
        banner = '<div class="join-banner"><img src="%sassets/img/join-banner.jpg" alt="%s"><div class="banner-cap"><p>%s</p></div></div>' % (pre, d["hero"], "<br>".join(d["intro_lines"]))
    imgdir = os.path.join(BASE, "assets", "img", "join")
    photos = sorted(f for f in os.listdir(imgdir) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))) if os.path.isdir(imgdir) else []
    gallery = ""
    if photos:
        figs = "".join('<figure><img src="%sassets/img/join/%s" alt="%s"><figcaption>%s</figcaption></figure>' % (pre, f, os.path.splitext(f)[0], os.path.splitext(f)[0]) for f in photos)
        gallery = '<div class="join-gallery reveal">%s</div>' % figs
    jobs = ""
    for t, loc, p in d["jobs"]:
        jobs += ('<div class="apps-col reveal">\n<div class="col-ico">%s</div><h4>%s</h4>\n'
                 '<span class="en">%s</span>\n<p>%s</p>\n</div>') % (ICO_PIN, t, loc, p)
    return """<section class="page-hero">
  <div class="bg"></div>
  <div class="inner">
    <p class="en">%s</p>
    <h1>%s</h1>
    <span class="bar"></span>
      <p style="color:#d8d2c8;font-size:15px;letter-spacing:2px;margin-top:20px">%s</p>
    </div>
</section>
%s
<section class="sec">
  <div class="wrap">
  <div class="sec-head reveal"><p class="en">Why VOYISL</p><h2>%s</h2><span class="bar"></span></div>
  <div class="agents-grid" style="margin-top:26px">
      %s
  </div>
  <p class="reveal" style="margin-top:44px;text-align:center;color:var(--muted);line-height:2">%s</p>
  <div class="sense-chips reveal" style="margin:14px 0 22px;justify-content:center">%s</div>\n  %s
  <div class="sec-head reveal"><p class="en">Office Locations</p><h2>%s</h2><span class="bar"></span></div>
  <p class="reveal" style="margin-top:18px;text-align:center;color:var(--muted);line-height:2">%s</p>
  <div class="city-grid reveal">%s</div>
  <div class="sec-head reveal" style="margin-top:44px"><p class="en">Open Positions</p><h2>%s</h2><span class="bar"></span></div>
  <div class="apps-grid" style="margin-top:18px">%s</div>
  <p class="reveal" style="margin-top:26px;color:var(--muted);font-size:13.5px">%s</p>
  <div class="asub-partners reveal" style="margin-top:34px"><h4>%s</h4><div class="desc">%s</div><div class="cust"><b>%s</b><span>%s</span></div></div>
  </div>
</section>
""" % (d["hero_en"], d["hero"], d["tagline"], banner, d["why_title"], whys,
       d["culture_desc"], chips, gallery, d["loc_title"],
       d["loc_desc"], cities,
       d["jobs_title"], jobs, d["jobs_note"], d["apply_t"], d["apply_p"], d["apply_b"], d["apply_s"])

DESC = {
 "cn": "加入寅家科技（VOYISL），与跨领域智能应用先行者同行，共同推动智能感知、决策与控制技术的规模化应用。",
 "tw": "加入寅家科技（VOYISL），與跨領域智能應用先行者同行，共同推動智能感知、決策與控制技術的規模化應用。",
 "en": "Join VOYISL and work alongside pioneers of cross-domain intelligent applications, scaling perception, decision and control technologies into real-world products.",
}

D = {
"cn": {
 "hero": "加入我们", "hero_en": "Join Us",
 "tagline": "与优秀者同行，共赴智能出行新未来",
 "intro_lines": ["寅家科技正处于从汽车智能化向多领域通用智能体拓展的加速期。",
               "我们相信，优秀的作品源于优秀的团队——",
               "在这里，你将与一群对技术充满热情的伙伴并肩，",
               "把实验室里的算法变成百万用户每天都在使用的产品。"],
 "why_title": "为什么选择寅家",
 "why": [("全栈技术平台", "覆盖视觉感知、融合定位、决策控制的全栈自研体系，深入量产一线，做真正落地的技术。"),
        ("成长与培养", "完善的新人培训与导师制度，管理与专业双通道发展路径，你的努力总会被看见。"),
        ("全球化舞台", "研发与智造中心遍布全国，海外办事处联动全球客户，视野与业务同样无界。"),
        ("有温度的团队", "开放的办公环境与平等沟通氛围，表彰会、生日会、品牌日，让每一份付出都有回响。")],
 "culture_title": "寅家人文化", "culture_desc": "工作之外，我们同样认真生活。",
 "culture": ["开放的办公环境", "员工表彰会", "寅家人面对面", "生日会", "品牌日", "新人培训", "文体活动"],
 "loc_title": "办公地点",
 "loc_desc": "研发 & 智造中心遍布全国 7 城，覆盖研发、测试与智能制造全链条。",
 "cities": ["上海", "厦门", "苏州", "嘉兴", "芜湖", "东莞", "台湾"],
 "stat1": ("7 城", "研发 & 智造中心"), "stat2": ("5 地", "海外办事处"),
 "loc1_t": "研发 & 智造中心", "loc1_p": "上海、厦门、苏州、嘉兴、芜湖、东莞、台湾，覆盖研发、测试与智能制造全链条。",
 "loc2_t": "海外办事处", "loc2_p": "中国香港、越南河内、日本东京、德国法兰克福、巴西圣保罗，高效触达全球客户。",
 "jobs_title": "热招职位",
 "jobs": [("技术经理（农机）", "上海 / 苏州", "作为技术领头人对具体项目实现进行技术拆解、工作分解，拉动公司资源池完成项目，并对产品开发的各个部分进行技术质量把控；跟踪业内技术发展趋势，从宏观上搭建技术实现框架和验证框架。"),
         ("嵌入式软件工程师", "苏州", "负责汽车电子软件开发，熟练掌握嵌入式 C/C++ 编程。"),
         ("高级感知算法工程师", "苏州", "负责计算机视觉或深度学习算法相关的前沿技术研发工作。"),
         ("项目经理", "上海 / 苏州", "作为项目第一责任人，全面主导客户定点项目和预研项目的全流程项目开发管理工作。"),
         ("海外市场业务助理", "上海", "协助公司开拓海外市场。"),
         ("海外销售总监", "上海", "负责东南亚、中东非、欧美、日韩等重点区域年度销售策略、分解目标并达成营收与利润指标。")],
 "jobs_note": "* 以上职位长期开放，更多岗位持续更新中。",
 "apply_t": "简历投递", "apply_p": "请将简历发送至招聘邮箱，邮件主题格式：应聘岗位 + 姓名 + 工作地点。我们将在收到简历后尽快与您联系。",
 "apply_b": "hr@voyager-tech.com", "apply_s": "商务合作与市场咨询，请前往<a href=\"contact.html\">联系页面</a>，或发送邮件至 sales@voyager-tech.com",
},
"tw": {
 "hero": "加入我們", "hero_en": "Join Us",
 "tagline": "與優秀者同行，共赴智能出行新未來",
 "intro_lines": ["寅家科技正處於從汽車智能化向多領域通用智能體拓展的加速期。",
               "我們相信，優秀的作品源於優秀的團隊——",
               "在這裡，你將與一群對技術充滿熱情的夥伴並肩，",
               "把實驗室裡的演算法變成百萬用戶每天都在使用的產品。"],
 "why_title": "為什麼選擇寅家",
 "why": [("全棧技術平臺", "覆蓋視覺感知、融合定位、決策控制的全棧自研體系，深入量產一線，做真正落地的技術。"),
        ("成長與培養", "完善的新人培訓與導師制度，管理與專業雙通道發展路徑，你的努力總會被看見。"),
        ("全球化舞臺", "研發與智造中心遍佈全國，海外辦事處聯動全球客戶，視野與業務同樣無界。"),
        ("有溫度的團隊", "開放的辦公環境與平等溝通氛圍，表彰會、生日會、品牌日，讓每一份付出都有迴響。")],
 "culture_title": "寅家人文化", "culture_desc": "工作之外，我們同樣認真生活。",
 "culture": ["開放的辦公環境", "員工表彰會", "寅家人面對面", "生日會", "品牌日", "新人培訓", "文體活動"],
 "loc_title": "辦公地點",
 "loc_desc": "研發 & 智造中心遍佈全國 7 城，覆蓋研發、測試與智能製造全鏈條。",
 "cities": ["上海", "廈門", "蘇州", "嘉興", "蕪湖", "東莞", "臺灣"],
 "stat1": ("7 城", "研發 & 智造中心"), "stat2": ("5 地", "海外辦事處"),
 "loc1_t": "研發 & 智造中心", "loc1_p": "上海、廈門、蘇州、嘉興、蕪湖、東莞、臺灣，覆蓋研發、測試與智能製造全鏈條。",
 "loc2_t": "海外辦事處", "loc2_p": "中國香港、越南河內、日本東京、德國法蘭克福、巴西聖保羅，高效觸達全球客戶。",
 "jobs_title": "熱招職位",
 "jobs": [("技術經理（農機）", "上海 / 蘇州", "作為技術領頭人對具體項目實現進行技術拆解、工作分解，拉動公司資源池完成項目，並對產品開發的各個部分進行技術質量把控；跟蹤業內技術發展趨勢，從宏觀上搭建技術實現框架和驗證框架。"),
         ("嵌入式軟體工程師", "蘇州", "負責汽車電子軟體開發，熟練掌握嵌入式 C/C++ 編程。"),
         ("高級感知演算法工程師", "蘇州", "負責計算機視覺或深度學習演算法相關的前沿技術研發工作。"),
         ("項目經理", "上海 / 蘇州", "作為項目第一責任人，全面主導客戶定點項目和預研項目的全流程項目開發管理工作。"),
         ("海外市場業務助理", "上海", "協助公司開拓海外市場。"),
         ("海外銷售總監", "上海", "負責東南亞、中東非、歐美、日韓等重點區域年度銷售策略、分解目標並達成營收與利潤指標。")],
 "jobs_note": "* 以上職位長期開放，更多崗位持續更新中。",
 "apply_t": "簡歷投遞", "apply_p": "請將簡歷發送至招聘郵箱，郵件主題格式：應聘崗位 + 姓名 + 工作地點。我們將在收到簡歷後儘快與您聯絡。",
 "apply_b": "hr@voyager-tech.com", "apply_s": "商務合作與市場諮詢，請前往<a href=\"contact.html\">聯絡頁面</a>，或發送郵件至 sales@voyager-tech.com",
},
"en": {
 "hero": "Join Us", "hero_en": "Join Us",
 "tagline": "Grow with the best, toward the future of smart mobility",
 "intro_lines": ["VOYISL is accelerating from automotive intelligence toward general intelligent agents across multiple domains.",
               "We believe great products come from great teams —",
               "here, you will work alongside passionate partners",
               "and turn algorithms from the lab into products used by millions every day."],
 "why_title": "Why VOYISL",
 "why": [("Full-Stack Platform", "A full-stack in-house system spanning visual perception, fusion positioning and decision control — working on technology that truly ships."),
        ("Growth & Development", "Structured onboarding and mentorship, with dual career tracks in management and expertise — your effort is always seen."),
        ("A Global Stage", "R&D and manufacturing centers across China and offices worldwide — a business and a horizon without borders."),
        ("A Team with Warmth", "An open office and equal communication, with recognition events, birthday celebrations and brand days that make every contribution count.")],
 "culture_title": "Life at VOYISL", "culture_desc": "Beyond work, we take life seriously too.",
 "culture": ["Open office environment", "Employee recognition", "Face-to-face with VOYISLers", "Birthday celebrations", "Brand day", "New-hire training", "Sports & culture"],
 "loc_title": "Office Locations",
 "loc_desc": "R&D and manufacturing centers across 7 cities, covering the full chain of R&D, testing and intelligent manufacturing.",
 "cities": ["Shanghai", "Xiamen", "Suzhou", "Jiaxing", "Wuhu", "Dongguan", "Taiwan"],
 "stat1": ("7 Cities", "R&D & Manufacturing Centers"), "stat2": ("5 Offices", "Overseas Locations"),
 "loc1_t": "R&D & Manufacturing Centers", "loc1_p": "Shanghai, Xiamen, Suzhou, Jiaxing, Wuhu, Dongguan and Taiwan — covering the full chain of R&D, testing and intelligent manufacturing.",
 "loc2_t": "Overseas Offices", "loc2_p": "Hong Kong (China), Hanoi (Vietnam), Tokyo (Japan), Frankfurt (Germany) and São Paulo (Brazil) — staying close to customers worldwide.",
 "jobs_title": "Open Positions",
 "jobs": [("Technical Manager (Agricultural Machinery)", "Shanghai / Suzhou", "As technical lead, break down project implementation into technical and work packages, mobilize company resources to deliver, and control technical quality across product development; track industry technology trends and build high-level implementation and validation frameworks."),
         ("Embedded Software Engineer", "Suzhou", "Develop automotive electronics software; proficient in embedded C/C++ programming."),
         ("Senior Perception Algorithm Engineer", "Suzhou", "Drive cutting-edge R&D in computer vision and deep-learning algorithms."),
         ("Project Manager", "Shanghai / Suzhou", "As the primary owner, lead full-lifecycle development management of customer-nominated and pre-research projects."),
         ("Overseas Marketing Assistant", "Shanghai", "Support the company in expanding overseas markets."),
         ("Overseas Sales Director", "Shanghai", "Own annual sales strategies for key regions including Southeast Asia, Middle East & Africa, Europe & the Americas, Japan & Korea; break down targets and deliver revenue and profit goals.")],
 "jobs_note": "* These positions are open long-term; more openings are added regularly.",
 "apply_t": "How to Apply", "apply_p": "Please send your resume to our recruiting mailbox with the subject line: Position + Name + Preferred location. We will get back to you as soon as possible.",
 "apply_b": "hr@voyager-tech.com", "apply_s": "For business inquiries, please visit the <a href=\"contact.html\">contact page</a> or email sales@voyager-tech.com",
},
}

for lang in ("cn", "tw", "en"):
    pre = "" if lang == "cn" else "../"
    d = D[lang]
    html = header(lang, pre, d["hero"], DESC[lang]) + body(lang, pre, d) + footer(lang, pre)
    outdir = BASE if lang == "cn" else os.path.join(BASE, "zh-Hant" if lang == "tw" else "en")
    out = os.path.join(outdir, "join.html")
    with io.open(out, "w", encoding="utf-8") as f:
        html = re.sub(r'<p class="en">([^<]+)</p>(\s*)<h2([^>]*)>\1</h2>', r'<h2\3>\1</h2>', html)  # dedup eyebrow==h2
    f.write(html)
    print("write", out)
print("DONE")