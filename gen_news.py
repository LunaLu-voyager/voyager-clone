# -*- coding: utf-8 -*-
import urllib.request, ssl, warnings, re, json, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
warnings.filterwarnings("ignore")
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
UA = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36","Accept-Encoding":"identity"}
BASE = r"C:\Users\VT86\Documents\Codex\2026-08-18\c\outputs\voyager-clone"
IDS = [148,146,133,131,127,126,125,124]
def fetch(nid):
    req = urllib.request.Request("https://www.voyager-tech.com/nd.jsp?id=%d" % nid, headers=UA)
    with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
        html = r.read().decode("utf-8","ignore")
    m = re.search(r"window\.renderData = (\{.*?\});\s*</script>", html, re.S)
    d = json.loads(m.group(1))
    ni = d["modules"]["module2"]["newsInfo"]
    c = ni.get("content","") or ni.get("richContent","")
    c = c.replace('src="//', 'src="https://').replace("src='//", "src='https://")
    return ni.get("title",""), c
DATA = {}
for nid in IDS:
    try:
        t, c = fetch(nid)
        DATA[str(nid)] = {"title": t, "content": c}
        print("fetch", nid, "OK", len(c))
    except Exception as e:
        print("fetch", nid, "ERR", repr(e)[:100])
EN_T = {
 "148": "Gathering Strength in Brazil | VOYISL Partners with MEKRA Lang and Metagal at Mercedes-Benz Tech Day",
 "146": "GB 47955 Takes Effect | Meeting L2 Safety with the Eye-Brain-Body Framework",
 "133": "Dreams Awaken in Summer | Pearl Youths at VOYISL",
 "131": "VOYISL at WAIC | Mass-Production Physical AI Solutions",
 "127": "Meet AI, Meet VOYISL | Join Us at WAIC 2026",
 "126": "Yicai Interview | Dialogue with Brian Chen, CEO of VOYISL",
 "125": "Dragon Boat Festival | Academia & Enterprise Sail Together",
 "124": "VOYISL Named 2026 GoGlobal Emerging Mobility Brands TOP10",
}
def header_tpl(lang):
    rel = "zh-Hant/" if lang=="tw" else "en/" if lang=="en" else ""
    tpl = open(os.path.join(BASE, rel+"news.html"), encoding="utf-8").read()
    h = tpl.find("<header"); he = tpl.find("</header>")+len("</header>")
    f = tpl.find("<footer"); fe = tpl.find("</footer>")+len("</footer>")
    head = re.search(r"<head>[\s\S]*?</head>", tpl).group(0)
    return head, tpl[h:he], tpl[f:fe]
def build_detail(lang, nid):
    d = DATA[nid]
    head, header, footer = header_tpl(lang)
    title = d["title"] if lang in ("cn","tw") else EN_T.get(nid, d["title"])
    head2 = re.sub(r"<title>.*?</title>", "<title>\u5bc5\u5bb6\u79d1\u6280 VOYISL - %s</title>" % title, head, count=1)
    header2 = re.sub(r'class="active"', "", header)
    body = ("<body>\n%s\n<section class=\"page-hero\">\n  <div class=\"bg\"></div>\n  <div class=\"inner\">\n    <p class=\"en\">News</p>\n    <h1>%s</h1>\n    <span class=\"bar\"></span>\n  </div>\n</section>\n"
            "<section class=\"sec\">\n  <div class=\"wrap\">\n    <article class=\"news-detail\">%s</article>\n  </div>\n</section>\n%s\n"
            "<script src=\"%sassets/js/main.js\"></script>\n</body>\n</html>") % (header2, title, d["content"], footer, "../" if lang!="cn" else "")
    page = "<!DOCTYPE html>\n<html lang=\"%s\">\n%s\n%s" % ({"cn":"zh-CN","tw":"zh-Hant","en":"en"}[lang], head2, body)
    out = os.path.join(BASE, ("" if lang=="cn" else "zh-Hant/" if lang=="tw" else "en/")) + "news-detail-%s.html" % nid
    open(out, "w", encoding="utf-8").write(page)
    print("detail", lang, nid)
for lang in ("cn","tw","en"):
    for nid in [str(x) for x in IDS]:
        build_detail(lang, nid)
print("DONE")
