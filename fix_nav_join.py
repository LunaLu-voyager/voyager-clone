# -*- coding: utf-8 -*-
# Replace "Contact Us" nav/footer entries with "Join Us" across all pages.
import os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = r"C:\Users\VT86\Documents\Codex\2026-08-18\c\outputs\voyager-clone"
DIRS = {"cn": BASE, "tw": os.path.join(BASE, "zh-Hant"), "en": os.path.join(BASE, "en")}
REPL = {
 "cn": [('<a href="contact.html" class="active">联系我们</a>', '<a href="join.html">加入我们</a>'),
        ('<a href="contact.html">联系我们</a>', '<a href="join.html">加入我们</a>')],
 "tw": [('<a href="contact.html" class="active">聯絡我們</a>', '<a href="join.html">加入我們</a>'),
        ('<a href="contact.html">聯絡我們</a>', '<a href="join.html">加入我們</a>')],
 "en": [('<a href="contact.html" class="active">Contact</a>', '<a href="join.html">Join Us</a>'),
        ('<a href="contact.html">Contact</a>', '<a href="join.html">Join Us</a>')],
}
for lang, d in DIRS.items():
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".html") or fn == "join.html": continue
        p = os.path.join(d, fn)
        s = io.open(p, encoding="utf-8").read()
        total = 0
        for old, new in REPL[lang]:
            n = s.count(old)
            if n: s = s.replace(old, new); total += n
        if total:
            io.open(p, "w", encoding="utf-8").write(s)
            print("%s/%s: %d replaced" % (lang, fn, total))
print("DONE")