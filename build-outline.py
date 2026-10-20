#!/usr/bin/env python3
"""Build the outline PDF from advertising-outline.md (elegant-pdf design system).

Source format:
  # Title
  (blank)
  EYEBROW LINE
  meta line
  (blank)
  ## <chip> · <section title>
  - bullet
  - bullet
  ...
  ## About the speaker
  <paragraph>
"""
import subprocess, sys, html, pathlib

SD = "/Users/kerryback/.claude/plugins/cache/kerryback-skills/elegant-pdf/0.1.0/skills/elegant-pdf"
BODY = 11.8   # body text px — the knob to turn if the page count changes

src = pathlib.Path("advertising-outline.md").read_text()
blocks = [b.strip() for b in src.split("\n\n") if b.strip()]

title = blocks[0].lstrip("# ").strip()
eyebrow, metaline = blocks[1].split("\n")[:2]

items, bio = [], ""
chip = name = None
pending = []

def flush():
    if name is not None:
        items.append((chip, name, " · ".join(pending)))

for b in blocks[2:]:
    if b.startswith("## "):
        head = b[3:].strip()
        if head.lower().startswith("about the speaker"):
            flush()
            chip = name = None
            continue
        flush()
        c, _, n = head.partition("·")
        chip, name, pending = c.strip(), n.strip(), []
    elif chip is None and name is None and items:
        bio = b.replace("\n", " ")
    else:
        pending += [ln.lstrip("- ").strip() for ln in b.split("\n") if ln.strip().startswith("-")]
flush()

def esc(t):
    t = html.escape(t, quote=False)
    return (t.replace("—", "&mdash;").replace("–", "&ndash;")
             .replace("·", "&middot;").replace("'", "&rsquo;").replace("'", "&rsquo;"))

rows = []
for c, n, desc in items:
    d = f'\n      <div class="item-desc">{esc(desc)}</div>' if desc else ""
    rows.append(f'    <div class="item"><div class="chip">{esc(c)}</div><div>\n'
                f'      <div class="item-title">{esc(n)}</div>{d}</div></div>')

biohtml = (f'\n    <div class="section-head bio-head"><span class="label">About the speaker</span></div>\n'
           f'    <div class="headrule"></div>\n'
           f'    <div class="bio">{esc(bio)}</div>') if bio else ""

doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="theme.css">
<style>
  /* elegant-pdf default palette (Rice navy + gold), compact page */
  .page {{ padding: 0.7in 0.8in 0.65in; }}
  .page .eyebrow {{ font-size: 9.5px; letter-spacing: 3.2px; color: var(--navy); margin-bottom: 9px; }}
  .page .display {{ font-size: 30px; }}
  .page > .rule {{ margin: 12px 0 10px; height: 3px; }}
  .metaline {{ font-size: 11px; color: var(--gray); }}
  .page .section-head {{ margin-top: 20px; }}
  .page .section-head .label {{ font-size: 14px; font-weight: 800; }}
  .headrule {{ height: 2px; border-radius: 2px; margin: 6px 0 2px;
    background: linear-gradient(90deg, var(--navy) 0 62%, var(--gold) 62% 100%); }}
  .page .item {{ gap: 15px; padding: 10px 0; }}
  .page .chip {{ flex-basis: 56px; font-size: 9.5px; padding: 5px 0; border-radius: 4px;
    letter-spacing: .5px; }}
  .page .item-title {{ font-size: 14px; line-height: 1.25; }}
  .page .item-desc {{ font-size: {BODY}px; line-height: 1.55; color: var(--gray); margin-top: 3px; }}
  .bio-head {{ margin-top: 22px !important; }}
  .bio {{ font-size: 10.6px; line-height: 1.6; color: var(--gray); margin-top: 10px; }}
</style>
</head>
<body>

  <section class="page">
    <div class="eyebrow">{esc(eyebrow)}</div>
    <h1 class="display">{esc(title)}</h1>
    <div class="rule"></div>
    <div class="metaline">{esc(metaline)}</div>

    <div class="section-head"><span class="label">Program</span></div>
    <div class="headrule"></div>

{chr(10).join(rows)}
{biohtml}
  </section>

</body>
</html>
"""
pathlib.Path("outline-doc.html").write_text(doc)
subprocess.run(["bash", f"{SD}/assets/render.sh", "pdf", "outline-doc.html", "ai-and-business-schools.pdf"],
               check=True, stderr=subprocess.DEVNULL)
print(subprocess.run(["pdfinfo", "ai-and-business-schools.pdf"], capture_output=True, text=True)
      .stdout.split("Pages:")[1].split("\n")[0].strip(), "pages")
