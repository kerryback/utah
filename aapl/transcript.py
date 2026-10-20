import re, sys, html as H

def strip(t):
    t = re.sub(r"<(script|style|svg|button)\b.*?</\1>", " ", t, flags=re.S|re.I)
    t = re.sub(r"<strong[^>]*>(.*?)</strong>", r"\1", t, flags=re.S|re.I)
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"[ \t]+", " ", H.unescape(t)).strip()

def extract(path):
    s = open(path, encoding="utf-8", errors="replace").read()
    start = s.find('class="article-body')
    end = s.find('article-body-promobox', start)
    body = s[start:end if end > start else None]
    out = []
    for m in re.finditer(r"<(p|h2|h3|h4)\b[^>]*>(.*?)</\1>", body, re.S|re.I):
        tag, txt = m.group(1).lower(), strip(m.group(2))
        if not txt: continue
        out.append(("\n## " + txt if tag != "p" else txt))
    text = "\n\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text).strip()

if __name__ == "__main__":
    print(extract(sys.argv[1]))
