# -*- coding: utf-8 -*-
# Generate the three General Intelligent Agents sub-pages (agri / lowalt / robot)
# in Simplified Chinese (root), Traditional Chinese (zh-Hant/) and English (en/).
import os, io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = r"C:\Users\VT86\Documents\Codex\2026-08-18\c\outputs\voyager-clone"

def header(lang, pre, title, desc, hero_h1):
    if lang == "cn":
        nav = ('<a href="index.html">首页</a>\n      <a href="about.html">关于寅家</a>\n      <a href="tech.html">技术路线</a>'
               '<span class="has-drop"><a href="agents.html" class="active">通用智能体</a><span class="drop">'
               '<a href="agents-car.html">智能汽车</a><a href="agents-agri.html">农业机器人</a>'
               '<a href="agents-lowalt.html">低空经济</a><a href="agents-robot.html">具身机器人</a></span></span>\n      '
               '<a href="news.html">企业动态</a>\n      <a href="join.html">加入我们</a>')
        lang_switch = '<a href="index.html" class="on">简</a>\n        <a href="zh-Hant/index.html">繁</a>\n        <a href="en/index.html">EN</a>'
        menu = "菜单"
        html_lang = "zh-CN"
    elif lang == "tw":
        nav = ('<a href="../index.html">首頁</a>\n      <a href="about.html">關於寅家</a>\n      <a href="tech.html">技術路線</a>'
               '<span class="has-drop"><a href="agents.html" class="active">通用智能體</a><span class="drop">'
               '<a href="agents-car.html">智能汽車</a><a href="agents-agri.html">農業機器人</a>'
               '<a href="agents-lowalt.html">低空經濟</a><a href="agents-robot.html">具身機器人</a></span></span>\n      '
               '<a href="news.html">企業動態</a>\n      <a href="join.html">加入我們</a>')
        lang_switch = '<a href="../index.html">簡</a>\n        <a href="index.html" class="on">繁</a>\n        <a href="../en/index.html">EN</a>'
        menu = "選單"
        html_lang = "zh-Hant"
    else:
        nav = ('<a href="../index.html">Home</a>\n      <a href="about.html">About</a>\n      <a href="tech.html">Technology</a>'
               '<span class="has-drop"><a href="agents.html" class="active">Agents</a><span class="drop">'
               '<a href="agents-car.html">Intelligent Vehicle</a><a href="agents-agri.html">Agricultural Robot</a>'
               '<a href="agents-lowalt.html">Low-Altitude Economy</a><a href="agents-robot.html">Embodied Robot</a></span></span>\n      '
               '<a href="news.html">News</a>\n      <a href="join.html">Join Us</a>')
        lang_switch = '<a href="../index.html">简</a>\n        <a href="../zh-Hant/index.html">繁</a>\n        <a href="index.html" class="on">EN</a>'
        menu = "Menu"
        html_lang = "en"
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

ICO_EYE = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>'
ICO_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 21s-7-6.2-7-11a7 7 0 1 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>'
ICO_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 2 4 6v6c0 4.4 3.4 8.2 8 10 4.6-1.8 8-5.6 8-10V6z"/><path d="m9 12 2 2 4-4.5"/></svg>'

def body(lang, pre, d, slug):
    stats = "".join('<div class="stat-card"><div class="num">%s</div>%s</div>' % (n, ('<div class="lab">%s</div>' % l) if l else "") for n, l in d["stats"])
    secs = "".join('<div class="asub-sec reveal"><h4>%s</h4><p>%s</p></div>\n  ' % (h, p) for h, p in d["secs"])
    icos = [ICO_EYE, ICO_PIN, ICO_SHIELD]
    cols = ""
    for i, (t, en, items) in enumerate(d["apps"]):
        lis = "".join("<li>%s</li>" % x for x in items)
        cols += ('<div class="apps-col reveal">\n<div class="col-ico">%s</div><h4>%s</h4>\n'
                 '<span class="en">%s</span>\n<ul>\n%s\n</ul>\n</div>') % (icos[i], t, en, lis)
    cap = ""
    if slug not in ("agents-agri", "agents-lowalt", "agents-robot"):
        cap = '<div class="img-caption left"><span class="img-label">%s</span><p class="img-desc">%s</p></div>' % (d["img_label"], d["img_desc"])
    if "intro_lines" in d:
        intro_html = '<p class="reveal" style="max-width:900px;margin:0 auto 40px;text-align:center;color:var(--muted);line-height:2.2;font-size:15px">%s</p>' % "<br>".join(d["intro_lines"])
    else:
        intro_html = '<p class="reveal" style="max-width:840px;color:var(--muted);line-height:2;margin-bottom:34px">%s</p>' % d["intro"]
    scenes_html = ""
    if "scenes" in d:
        st, items = d["scenes"]
        cards = "".join('<div class="scene-card">%s</div>' % x for x in items)
        scenes_html = '<div class="scene-overlay"><h4 class="scene-title">%s</h4><div class="scene-grid">%s</div></div>' % (st, cards)
    img_cls = slug + (" has-scenes" if "scenes" in d else "")
    return """<section class="page-hero">
  <div class="bg"></div>
  <div class="inner">
    <p class="en">%s</p>
    <h1>%s</h1>
    <span class="bar"></span>
      <p style="color:#d8d2c8;font-size:15px;letter-spacing:2px;margin-top:20px">%s</p>
    </div>
</section>
<div class="agents-img full reveal %s"><img src="%sassets/img/%s" alt="%s">%s</div>
<section class="sec">
  <div class="wrap">
  %s
  <div class="asub-stat reveal">%s</div>
  %s
<div class="apps-block">
  <div class="sec-head reveal"><p class="en">Technology Reuse</p><h2>%s</h2><span class="bar"></span></div>
  <div class="apps-grid">%s</div>
</div></div>
</section>
""" % (d["hero_en"], d["hero"], d["tagline"], img_cls, pre, d["img"], d["hero"], cap + scenes_html,
       intro_html, stats, secs, d["apps_title"], cols)

DESC = {
 "cn": "寅家科技（VOYISL）专注于智能驾驶与泊车技术，提供视觉感知 VT-Sensing、融合定位 VT-Navi、决策控制 VT-Vulcan 全栈量产解决方案。",
 "tw": "寅家科技（VOYISL）專注於智慧駕駛與泊車技術，提供視覺感知 VT-Sensing、融合定位 VT-Navi、決策控制 VT-Vulcan 全棧量產解決方案。",
 "en": "VOYISL specializes in intelligent driving and parking technology, delivering full-stack mass-production solutions across visual perception VT-Sensing, fusion positioning VT-Navi and decision control VT-Vulcan.",
}

PAGES = {
"agents-agri": {
 "cn": {
  "hero": "农业机器人", "hero_en": "Agricultural Robot",
  "tagline": "VT-Mow：把车规级智能带进田间地头",
  "intro": "农业场景环境复杂、工况严苛，正是车规级智能技术的用武之地。寅家科技将十余年汽车量产验证的视觉感知、融合定位与决策控制技术迁移至农业领域，推出 VT-Mow 农业机器人解决方案，覆盖农耕作业、果园植保、农场巡检等场景，让农机看得见、行得稳、作业准。",
  "intro_lines": ["农业场景环境复杂、工况严苛，正是车规级智能技术的用武之地。",
                "寅家科技将十余年汽车量产验证的视觉感知、融合定位与决策控制技术迁移至农业领域，",
                "推出 VT-Mow 农业机器人解决方案，覆盖农耕作业、果园植保、农场巡检等场景，",
                "让农机看得见、行得稳、作业准。"],
  "scenes": ("应用场景", ["果园植保", "除草", "运输", "夏剪枝头", "其他表层土浅耕农艺工作"]),
  "stats": [("全栈自研", "感知 · 定位 · 控制核心技术"), ("车规级", "高低温、振动、粉尘严苛环境验证")],
  "img": "agent-agri.jpg", "img_label": "智慧农业",
  "img_desc": "面向非结构化农田环境，提供环境感知、路径规划与作业控制一体化能力，助力农业装备智能化升级",
  "secs": [],
  "apps_title": "技术复用",
  "apps": [("VT-Sensing", "农田环境感知", ["作物行与田埂识别", "障碍物检测与绕行", "夜间及逆光作业感知"]),
           ("VT-Navi", "田间融合定位", ["GNSS + 视觉 + 惯导融合", "厘米级作业路径跟踪", "信号遮挡下可靠定位"]),
           ("VT-Vulcan®", "作业决策控制", ["全田块作业路径规划", "作业速度自适应控制", "机具协同与安全保护"])],
 },
 "tw": {
  "hero": "農業機器人", "hero_en": "Agricultural Robot",
  "tagline": "VT-Mow：把車規級智能帶進田間地頭",
  "intro": "農業場景環境複雜、工況嚴苛，正是車規級智能技術的用武之地。寅家科技將十餘年汽車量產驗證的視覺感知、融合定位與決策控制技術遷移至農業領域，推出 VT-Mow 農業機器人解決方案，覆蓋農耕作業、果園植保、農場巡檢等場景，讓農機看得見、行得穩、作業準。",
  "intro_lines": ["農業場景環境複雜、工況嚴苛，正是車規級智能技術的用武之地。",
                "寅家科技將十餘年汽車量產驗證的視覺感知、融合定位與決策控制技術遷移至農業領域，",
                "推出 VT-Mow 農業機器人解決方案，覆蓋農耕作業、果園植保、農場巡檢等場景，",
                "讓農機看得見、行得穩、作業準。"],
  "scenes": ("應用場景", ["果園植保", "除草", "運輸", "夏剪枝頭", "其他表層土淺耕農藝工作"]),
  "stats": [("全棧自研", "感知 · 定位 · 控制核心技術"), ("車規級", "高低溫、振動、粉塵嚴苛環境驗證")],
  "img": "agent-agri.jpg", "img_label": "智慧農業",
  "img_desc": "面向非結構化農田環境，提供環境感知、路徑規劃與作業控制一體化能力，助力農業裝備智能化升級",
  "secs": [],
  "apps_title": "技術複用",
  "apps": [("VT-Sensing", "農田環境感知", ["作物行與田埂識別", "障礙物檢測與繞行", "夜間及逆光作業感知"]),
           ("VT-Navi", "田間融合定位", ["GNSS + 視覺 + 慣導融合", "厘米級作業路徑跟蹤", "訊號遮擋下可靠定位"]),
           ("VT-Vulcan®", "作業決策控制", ["全田塊作業路徑規劃", "作業速度自適應控制", "機具協同與安全保護"])],
 },
 "en": {
  "hero": "Agricultural Robot", "hero_en": "Agricultural Robot",
  "tagline": "VT-Mow: bringing automotive-grade intelligence to the fields",
  "intro": "Agricultural environments are complex and demanding — exactly where automotive-grade intelligence proves its worth. VOYISL transfers the visual perception, fusion positioning and decision-control technologies proven in over a decade of automotive mass production into agriculture. The VT-Mow agricultural robot solution covers farming operations, orchard plant protection and farm inspection, helping machinery see clearly, drive steadily and work precisely.",
  "intro_lines": ["Agricultural environments are complex and demanding — exactly where automotive-grade intelligence proves its worth.",
                "VOYISL transfers the visual perception, fusion positioning and decision-control technologies proven in over a decade of automotive mass production into agriculture.",
                "The VT-Mow agricultural robot solution covers farming operations, orchard plant protection and farm inspection,",
                "helping machinery see clearly, drive steadily and work precisely."],
  "scenes": ("Applications", ["Orchard Plant Protection", "Weeding", "Transport", "Summer Pruning", "Other Surface Tillage Work"]),
  "stats": [("Full-Stack In-House", "Core perception, positioning and control technologies"), ("Automotive-Grade", "Validated against temperature extremes, vibration and dust")],
  "img": "agent-agri.jpg", "img_label": "Smart Agriculture",
  "img_desc": "Integrated perception, path planning and operation control for unstructured farmland, accelerating the intelligent upgrade of agricultural equipment",
  "secs": [],
  "apps_title": "Technology Reuse",
  "apps": [("VT-Sensing", "Farmland Perception", ["Crop-row and ridge recognition", "Obstacle detection and bypass", "Night and backlight operation perception"]),
           ("VT-Navi", "Field Fusion Positioning", ["GNSS + vision + IMU fusion", "Centimeter-level path tracking", "Reliable positioning under signal occlusion"]),
           ("VT-Vulcan®", "Operation Decision & Control", ["Full-field operation path planning", "Adaptive operation speed control", "Implement coordination and safety protection"])],
 },
},
"agents-lowalt": {
 "cn": {
  "hero": "低空经济", "hero_en": "Low-Altitude Economy",
  "tagline": "将经过整车量产验证的感知与导航技术移植到无人机平台",
  "intro": "低空飞行对感知与定位提出了更高要求。寅家科技将地面出行智能技术体系向上延伸，面向无人机巡检、低空物流、园区安防等场景，提供低空环境感知、融合定位与飞行决策控制能力，为飞行器装上“眼睛”和“大脑”。",
  "intro_lines": ["低空飞行对感知与定位提出了更高要求。",
                "寅家科技将地面出行智能技术体系向上延伸，",
                "面向无人机巡检、低空物流、园区安防等场景，提供低空环境感知、融合定位与飞行决策控制能力，",
                "为飞行器装上“眼睛”和“大脑”。"],
  "scenes": ("应用场景", ["应急救援作业", "物流配送业务", "车规级环境感知技术", "高精度定位能力", "特种场景巡检应用"]),
  "stats": [("通用的技术底座", ""), ("丰富的应用场景", "")],
  "img": "agent-lowalt.jpg", "img_label": "低空经济",
  "img_desc": "面向低空飞行器的感知、定位与决策解决方案，覆盖巡检、物流与安防等应用场景",
  "secs": [
   ("低空环境感知避障", "基于多目视觉与深度学习算法，识别电线、塔杆、建筑物等低空障碍物，实时输出障碍物方位与距离，为飞行器提供可靠的避障能力。"),
   ("复杂环境融合定位", "融合视觉、惯导与卫星定位，在楼宇之间、桥洞之下等卫星信号受限环境中，依然保持连续、稳定的位置感知与航迹保持。"),
   ("从地面到低空的技术延伸", "地面出行的感知、定位与控制技术与低空飞行器高度同源，经量产验证的软硬件体系可直接复用，加速低空装备的智能化落地与规模化应用。")],
  "apps_title": "技术复用",
  "apps": [("VT-Sensing", "低空环境感知", ["障碍物识别与测距", "电线、塔杆细目标检测", "全天候视觉感知"]),
           ("VT-Navi", "低空融合定位", ["视觉 + 惯导 + 卫星融合", "信号受限环境连续定位", "高精度航迹保持"]),
           ("VT-Vulcan®", "飞行决策控制", ["航线规划与动态调整", "自主避障决策", "功能安全架构"])],
 },
 "tw": {
  "hero": "低空經濟", "hero_en": "Low-Altitude Economy",
  "tagline": "將經過整車量產驗證的感知與導航技術移植到無人機平臺",
  "intro": "低空飛行對感知與定位提出了更高要求。寅家科技將地面出行智能技術體系向上延伸，面向無人機巡檢、低空物流、園區安防等場景，提供低空環境感知、融合定位與飛行決策控制能力，為飛行器裝上「眼睛」和「大腦」。",
  "intro_lines": ["低空飛行對感知與定位提出了更高要求。",
                "寅家科技將地面出行智能技術體系向上延伸，",
                "面向無人機巡檢、低空物流、園區安防等場景，提供低空環境感知、融合定位與飛行決策控制能力，",
                "為飛行器裝上「眼睛」和「大腦」。"],
  "scenes": ("應用場景", ["應急救援作業", "物流配送業務", "車規級環境感知技術", "高精度定位能力", "特種場景巡檢應用"]),
  "stats": [("通用的技術底座", ""), ("豐富的應用場景", "")],
  "img": "agent-lowalt.jpg", "img_label": "低空經濟",
  "img_desc": "面向低空飛行器的感知、定位與決策解決方案，覆蓋巡檢、物流與安防等應用場景",
  "secs": [
   ("低空環境感知避障", "基於多目視覺與深度學習演算法，識別電線、塔杆、建築物等低空障礙物，即時輸出障礙物方位與距離，為飛行器提供可靠的避障能力。"),
   ("複雜環境融合定位", "融合視覺、慣導與衛星定位，在樓宇之間、橋洞之下等衛星訊號受限環境中，依然保持連續、穩定的位置感知與航跡保持。"),
   ("從地面到低空的技術延伸", "地面出行的感知、定位與控制技術與低空飛行器高度同源，經量產驗證的軟硬體體系可直接複用，加速低空裝備的智能化落地與規模化應用。")],
  "apps_title": "技術複用",
  "apps": [("VT-Sensing", "低空環境感知", ["障礙物識別與測距", "電線、塔杆細目標檢測", "全天候視覺感知"]),
           ("VT-Navi", "低空融合定位", ["視覺 + 慣導 + 衛星融合", "訊號受限環境連續定位", "高精度航跡保持"]),
           ("VT-Vulcan®", "飛行決策控制", ["航線規劃與動態調整", "自主避障決策", "功能安全架構"])],
 },
 "en": {
  "hero": "Low-Altitude Economy", "hero_en": "Low-Altitude Economy",
  "tagline": "Perception and navigation technologies proven in vehicle mass production, transplanted to drone platforms",
  "intro": "Low-altitude flight raises the bar for perception and positioning. VOYISL extends its ground-mobility intelligence system upward, delivering low-altitude environmental perception, fusion positioning and flight decision-control capabilities for drone inspection, low-altitude logistics and park security — giving aircraft an \"eye\" and a \"brain\".",
  "intro_lines": ['Low-altitude flight raises the bar for perception and positioning.',
                'VOYISL extends its ground-mobility intelligence system upward,',
                'delivering low-altitude environmental perception, fusion positioning and flight decision-control capabilities for drone inspection, low-altitude logistics and park security —',
                'giving aircraft an "eye" and a "brain".'],
  "scenes": ("Applications", ["Emergency Rescue Operations", "Logistics & Delivery", "Automotive-Grade Environmental Perception", "High-Precision Positioning", "Special-Scenario Inspection"]),
  "stats": [("Versatile Tech Foundation", ""), ("Rich Application Scenarios", "")],
  "img": "agent-lowalt.jpg", "img_label": "Low-Altitude Economy",
  "img_desc": "Perception, positioning and decision solutions for low-altitude aircraft, covering inspection, logistics and security applications",
  "secs": [
   ("Low-Altitude Perception & Obstacle Avoidance", "Built on multi-camera vision and deep-learning algorithms, the system detects low-altitude obstacles such as power lines, towers and buildings, outputting their bearing and distance in real time to give aircraft reliable obstacle-avoidance capability."),
   ("Fusion Positioning in Complex Environments", "Fusing vision, inertial navigation and satellite positioning, the system maintains continuous, stable position awareness and trajectory holding even where satellite signals are limited — between buildings or under bridges."),
   ("From Ground to Sky", "Perception, positioning and control technologies for ground mobility are highly homologous to those of low-altitude aircraft. The mass-production-proven software and hardware stack can be reused directly, accelerating intelligent deployment and scaled adoption of low-altitude equipment.")],
  "apps_title": "Technology Reuse",
  "apps": [("VT-Sensing", "Low-Altitude Perception", ["Obstacle recognition and ranging", "Thin-target detection for wires and towers", "All-weather visual perception"]),
           ("VT-Navi", "Low-Altitude Fusion Positioning", ["Vision + IMU + satellite fusion", "Continuous positioning in signal-limited areas", "High-precision trajectory holding"]),
           ("VT-Vulcan®", "Flight Decision & Control", ["Route planning and dynamic adjustment", "Autonomous obstacle-avoidance decisions", "Functional safety architecture"])],
 },
},
"agents-robot": {
 "cn": {
  "hero": "具身机器人", "hero_en": "Embodied Robot",
  "tagline": "眼·脑·身，让 AI 走进物理世界",
  "intro": "具身智能是物理 AI 的下一站。寅家科技以“眼·脑·身”技术框架为核心，将视觉感知、智能决策与运动控制能力注入机器人本体，面向仓储物流、智能制造等产业园区，打造服务及工业机器人的智能化底座。",
  "intro_lines": ["具身智能是物理 AI 的下一站。",
                  "寅家科技以“眼·脑·身”技术框架为核心，",
                  "将视觉感知、智能决策与运动控制能力注入机器人本体，",
                  "面向仓储物流、智能制造等产业园区，打造服务及工业机器人的智能化底座。"],
  "scenes": ("应用场景", ["家庭、工厂及巡检场景", "自主导航与运动控制", "复杂地形识别", "环境感知与避障"]),
  "stats": [("全栈自研", "“眼·脑·身”技术框架"), ("多场景", "一次研发，多领域复用")],
  "img": "agent-robot.jpg", "img_label": "具身智能",
  "img_desc": "为机器人提供感知、决策与控制全栈能力，让机器在真实物理环境中看得懂、想得清、做得准",
  "secs": [
   ("眼 · 环境感知", "多目视觉与深度学习算法，让机器人实时理解周围环境：人员、货物、设备与通行空间一览无余，为自主行动提供感知基础。"),
   ("脑 · 智能决策", "基于量产验证的决策规划技术，让机器人在动态环境中自主规划路径、规避风险、完成任务，并与园区调度系统协同。"),
   ("身 · 运动控制", "车规级控制技术复用至机器人运动执行，保障启停平顺、转向精准、运行安全，适应产业园区的高强度作业节奏。")],
  "apps_title": "技术复用",
  "apps": [("VT-Sensing", "机器人感知", ["人员与障碍物检测", "货物与货架识别", "全向环境感知"]),
           ("VT-Navi", "园区定位导航", ["室内外连续定位", "高精地图与自主导航", "多机协同调度支持"]),
           ("VT-Vulcan®", "运动规划控制", ["路径规划与跟踪", "动态避障", "安全停车保护"])],
 },
 "tw": {
  "hero": "具身機器人", "hero_en": "Embodied Robot",
  "tagline": "眼·腦·身，讓 AI 走進物理世界",
  "intro": "具身智能是物理 AI 的下一站。寅家科技以「眼·腦·身」技術框架為核心，將視覺感知、智能決策與運動控制能力注入機器人本體，面向倉儲物流、智能製造等產業園區，打造服務及工業機器人的智能化底座。",
  "intro_lines": ["具身智能是物理 AI 的下一站。",
                  "寅家科技以「眼·腦·身」技術框架為核心，",
                  "將視覺感知、智能決策與運動控制能力注入機器人本體，",
                  "面向倉儲物流、智能製造等產業園區，打造服務及工業機器人的智能化底座。"],
  "scenes": ("應用場景", ["家庭、工廠及巡檢場景", "自主導航與運動控制", "複雜地形識別", "環境感知與避障"]),
  "stats": [("全棧自研", "「眼·腦·身」技術框架"), ("多場景", "一次研發，多領域複用")],
  "img": "agent-robot.jpg", "img_label": "具身智能",
  "img_desc": "為機器人提供感知、決策與控制全棧能力，讓機器在真實物理環境中看得懂、想得清、做得準",
  "secs": [
   ("眼 · 環境感知", "多目視覺與深度學習演算法，讓機器人即時理解周圍環境：人員、貨物、設備與通行空間一覽無餘，為自主行動提供感知基礎。"),
   ("腦 · 智能決策", "基於量產驗證的決策規劃技術，讓機器人在動態環境中自主規劃路徑、規避風險、完成任務，並與園區調度系統協同。"),
   ("身 · 運動控制", "車規級控制技術複用至機器人運動執行，保障啟停平順、轉向精準、運行安全，適應產業園區的高強度作業節奏。")],
  "apps_title": "技術複用",
  "apps": [("VT-Sensing", "機器人感知", ["人員與障礙物檢測", "貨物與貨架識別", "全向環境感知"]),
           ("VT-Navi", "園區定位導航", ["室內外連續定位", "高精地圖與自主導航", "多機協同調度支援"]),
           ("VT-Vulcan®", "運動規劃控制", ["路徑規劃與跟蹤", "動態避障", "安全停車保護"])],
 },
 "en": {
  "hero": "Embodied Robot", "hero_en": "Embodied Robot",
  "tagline": "Eye, brain and body — bringing AI into the physical world",
  "intro": "Embodied intelligence is the next stop for physical AI. Centered on the \"Eye-Brain-Body\" framework, VOYISL injects visual perception, intelligent decision-making and motion-control capabilities into robot platforms, building an intelligent foundation for service and industrial robots in industrial parks such as warehousing, logistics and smart manufacturing.",
  "intro_lines": ["Embodied intelligence is the next stop for physical AI.",
                  "Centered on the \"Eye-Brain-Body\" framework,",
                  "VOYISL injects visual perception, intelligent decision-making and motion control into robot platforms,",
                  "building an intelligent foundation for service and industrial robots in warehousing, logistics and smart manufacturing."],
  "scenes": ("Applications", ["Homes, Factories & Inspection", "Autonomous Navigation & Motion Control", "Complex Terrain Recognition", "Perception & Obstacle Avoidance"]),
  "stats": [("Full-Stack In-House", "The \"Eye-Brain-Body\" technology framework"), ("Multi-Scenario", "Develop once, reuse across domains")],
  "img": "agent-robot.jpg", "img_label": "Embodied Intelligence",
  "img_desc": "Full-stack perception, decision and control capabilities for robots — seeing clearly, thinking fast and acting precisely in real physical environments",
  "secs": [
   ("Eye · Environmental Perception", "Multi-camera vision and deep-learning algorithms let robots understand their surroundings in real time — people, goods, equipment and passable space — providing the perceptual foundation for autonomous operation."),
   ("Brain · Intelligent Decision-Making", "Built on mass-production-proven planning technology, robots plan paths autonomously in dynamic environments, avoid risks, complete tasks and coordinate with park dispatching systems."),
   ("Body · Motion Control", "Automotive-grade control technology is reused for robot motion execution, ensuring smooth start-stop behavior, precise steering and safe operation under the high-intensity pace of industrial parks.")],
  "apps_title": "Technology Reuse",
  "apps": [("VT-Sensing", "Robot Perception", ["People and obstacle detection", "Goods and shelving recognition", "Omnidirectional environmental perception"]),
           ("VT-Navi", "Park Positioning & Navigation", ["Continuous indoor-outdoor positioning", "HD maps and autonomous navigation", "Multi-robot dispatch support"]),
           ("VT-Vulcan®", "Motion Planning & Control", ["Path planning and tracking", "Dynamic obstacle avoidance", "Safe-stop protection"])],
 },
},
}

for slug, langs in PAGES.items():
    for lang in ("cn", "tw", "en"):
        pre = "" if lang == "cn" else "../"
        d = langs[lang]
        html = header(lang, pre, d["hero"], DESC[lang], d["hero"]) + body(lang, pre, d, slug) + footer(lang, pre)
        outdir = BASE if lang == "cn" else os.path.join(BASE, "zh-Hant" if lang == "tw" else "en")
        out = os.path.join(outdir, slug + ".html")
        with io.open(out, "w", encoding="utf-8") as f:
            html = re.sub(r'<p class="en">([^<]+)</p>(\s*)<h2([^>]*)>\1</h2>', r'<h2\3>\1</h2>', html)  # dedup eyebrow==h2
            f.write(html)
        print("write", out)
print("DONE")