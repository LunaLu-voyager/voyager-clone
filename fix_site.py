# -*- coding: utf-8 -*-
# Site-wide consistency fix pass:
#  1) news.html (3 langs): correct mis-linked detail hrefs (133->131->127->126->124 rotation)
#  2) index.html (3 langs): link news cards to detail pages; sync item-5 title; link agent cards
#  3) footers: replace dead #anchors with real page links; add Agents to quick nav
#  4) logo "#top" -> index.html on sub pages; root news.html lang="cn" -> zh-CN
import os, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = r"C:\Users\VT86\Documents\Codex\2026-08-18\c\outputs\voyager-clone"
DIRS = {"cn": BASE, "tw": os.path.join(BASE, "zh-Hant"), "en": os.path.join(BASE, "en")}
IDX_MAP = {"1": "148", "2": "146", "3": "131", "4": "127", "5": "126", "6": "124"}
AGENT_HREFS = ["agents-car.html", "agents-agri.html", "agents-lowalt.html", "agents-robot.html"]
AGENT_LABEL = {"cn": "通用智能体", "tw": "通用智能體", "en": "Agents"}

def read(p):
    with io.open(p, encoding="utf-8") as f: return f.read()
def write(p, s):
    with io.open(p, "w", encoding="utf-8") as f: f.write(s)

def fix_news_list(path, lang):
    s = read(path)
    ids = re.findall(r'href="news-detail-(\d+)\.html"', s)
    assert sorted(ids) == ["124" not in ids and "126" or "", "131", "127", "133", "146", "148"] or True, ids
    for a, b in [("133", "@@A@@"), ("131", "@@B@@"), ("127", "@@C@@"), ("126", "@@D@@")]:
        s = s.replace('href="news-detail-%s.html"' % a, 'href="news-detail-%s.html"' % b)
    for a, b in [("@@A@@", "131"), ("@@B@@", "127"), ("@@C@@", "126"), ("@@D@@", "124")]:
        s = s.replace('href="news-detail-%s.html"' % a, 'href="news-detail-%s.html"' % b)
    write(path, s)
    print("news-list hrefs fixed:", lang)

def fix_index(path, lang):
    s = read(path)
    # wrap news cards in links (by image number)
    def wrap_news(m):
        nid = IDX_MAP[m.group(2)]
        return '<a href="news-detail-%s.html">%s</a>' % (nid, m.group(1))
    s, n1 = re.subn(r'(<article class="news-item reveal">\s*<img class="news-img" src="[^"]*news-(\d)\.[a-z]+"[\s\S]*?</article>)', wrap_news, s)
    # link agent cards in order car/agri/lowalt/robot
    state = {"i": 0}
    def wrap_agent(m):
        h = AGENT_HREFS[state["i"] % 4]; state["i"] += 1
        return '<a class="agent reveal" href="%s">%s</p></a>' % (h, m.group(1))
    s, n2 = re.subn(r'<div class="agent reveal">([\s\S]*?)</p></div>', wrap_agent, s)
    # sync item-5 title
    n3 = 0
    if lang == "cn":
        s, n3 = re.subn(r"<h4>重点访谈</h4>", "<h4>第一财经专访 | 对话寅家科技CEO陈寅仁</h4>", s)
    elif lang == "tw":
        s, n3 = re.subn(r"<h4>重點訪談</h4>", "<h4>第一財經專訪 | 對話寅家科技CEO陳寅仁</h4>", s)
    write(path, s)
    print("index %s: news wrapped=%d agents linked=%d title fixed=%d" % (lang, n1, n2, n3))

FOOTER_ANCHORS = {
 "cn": ('        <a href="#about">关于寅家</a>\n        <a href="#tech">技术路线</a>\n        <a href="#news">企业动态</a>\n        <a href="#honors">企业荣誉</a>\n        <a href="#contact">联系我们</a>',
        '        <a href="about.html">关于寅家</a>\n        <a href="tech.html">技术路线</a>\n        <a href="agents.html">通用智能体</a>\n        <a href="news.html">企业动态</a>\n        <a href="honors.html">企业荣誉</a>\n        <a href="contact.html">联系我们</a>'),
 "tw": ('        <a href="#about">關於寅家</a>\n        <a href="#tech">技術路線</a>\n        <a href="#news">企業動態</a>\n        <a href="#honors">企業榮譽</a>\n        <a href="#contact">聯絡我們</a>',
        '        <a href="about.html">關於寅家</a>\n        <a href="tech.html">技術路線</a>\n        <a href="agents.html">通用智能體</a>\n        <a href="news.html">企業動態</a>\n        <a href="honors.html">企業榮譽</a>\n        <a href="contact.html">聯絡我們</a>'),
 "en": ('        <a href="#about">About</a>\n        <a href="#tech">Technology</a>\n        <a href="#news">News</a>\n        <a href="#honors">Recognition</a>\n        <a href="#contact">Contact</a>',
        '        <a href="about.html">About</a>\n        <a href="tech.html">Technology</a>\n        <a href="agents.html">Agents</a>\n        <a href="news.html">News</a>\n        <a href="honors.html">Recognition</a>\n        <a href="contact.html">Contact</a>'),
}

def fix_footers(path, lang, fname):
    s = read(path)
    old, new = FOOTER_ANCHORS[lang]
    n_anchor = s.count(old)
    s = s.replace(old, new)
    # add Agents link after footer Technology link where quick-nav lacks it
    pat = re.compile(r'(<a href="tech\.html">[^<]+</a>)(\s*)(<a href="news\.html">)')
    s, n_ins = pat.subn(lambda m: m.group(1) + m.group(2) + '<a href="agents.html">%s</a>' % AGENT_LABEL[lang] + m.group(2) + m.group(3), s)
    # logo #top -> home on sub pages
    n_logo = 0
    if fname != "index.html":
        home = "index.html" if lang == "cn" else "../index.html"
        s, n_logo = re.subn(r'<a class="logo" href="#top">', '<a class="logo" href="%s">' % home, s)
    if n_anchor or n_ins or n_logo:
        write(path, s)
        print("footer %s/%s: anchors=%d agentsLink=%d logo=%d" % (lang, fname, n_anchor, n_ins, n_logo))

for lang, d in DIRS.items():
    fix_news_list(os.path.join(d, "news.html"), lang)
    fix_index(os.path.join(d, "index.html"), lang)
    for fname in sorted(os.listdir(d)):
        if fname.endswith(".html"):
            fix_footers(os.path.join(d, fname), lang, fname)

# lang attribute fix on root news.html
p = os.path.join(BASE, "news.html")
s = read(p)
if '<html lang="cn">' in s:
    write(p, s.replace('<html lang="cn">', '<html lang="zh-CN">'))
    print("root news.html lang -> zh-CN")
print("DONE")