import requests, re, time, json, pandas as pd
HEADERS = {"User-Agent": "Kerry Back kerryback@gmail.com"}
BASE = "https://www.sec.gov/Archives/edgar/data/320193/{}/{}"

def fetch(nod, f):
    r = requests.get(BASE.format(nod,f), headers=HEADERS); r.raise_for_status()
    time.sleep(0.25); return r.text

def parse(html):
    """R-file -> (list of column headers, list of (label, [values]))"""
    tbl = re.search(r"<table.*?</table>", html, re.S|re.I).group(0)
    rows = re.findall(r"<tr.*?</tr>", tbl, re.S|re.I)
    out=[]
    for tr in rows:
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S|re.I)
        txt=[]
        for c in cells:
            c = re.sub(r"<[^>]+>"," ", c)
            c = (c.replace("&nbsp;"," ").replace("&#160;"," ").replace("&amp;","&")
                  .replace("&#8217;","'").replace("&#8220;",'"').replace("&#8221;",'"'))
            txt.append(re.sub(r"\s+"," ",c).strip())
        if txt: out.append(txt)
    return out

def tonum(s):
    if s is None: return None
    s = s.strip().replace(",","").replace("$","").replace("%","")
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()")
    if s in ("","—","-","–"): return None
    try: v=float(s)
    except ValueError: return None
    return -v if neg else v
