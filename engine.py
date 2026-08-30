"""Statische sitegenerator zonder dependencies."""
import os, re, html, datetime

SITE_NAME = "Vencodakwerken.be"
SITE_DOMAIN = "vencodakwerken.be"
BASE = "https://vencodakwerken.be"
TAGLINE = "Onafhankelijke dakwerkengids voor Vlaanderen"
EMAIL = "info@vencodakwerken.be"
LOCALE = "nl-BE"

DD = "https://www.dendekker-dakbedekking.nl/"
DD_BRAND = "Den Dekker Dakbedekking"
DD_PHONE = "085 130 2723"

PAGES = []


def dd_link(path="", anchor=None):
    """Uitgaande link naar Den Dekker. Ankertekst: merknaam, kale URL of volledige URL."""
    url = DD + path.lstrip("/")
    label = anchor or DD_BRAND
    return ('<a class="ext" href="%s" rel="nofollow noopener" target="_blank">%s</a>'
            % (url, label))


def dd_url(path=""):
    return DD + path.lstrip("/")


NAV = [
    ("/", "Home"),
    ("/over/", "Over"),
    ("/dakwerken/", "Dakwerken"),
    ("/regelgeving/", "Regels en premies"),
    ("/hulpmiddelen/", "Hulpmiddelen"),
    ("/locaties/", "Locaties"),
    ("/nieuws/", "Nieuws"),
    ("/contact/", "Contact"),
]

FOOTER_COLS = [
    ("Dakwerken", [
        ("/dakwerken/hellend-dak/", "Hellend dak"),
        ("/dakwerken/plat-dak/", "Plat dak"),
        ("/dakwerken/dakisolatie/", "Dakisolatie"),
        ("/dakwerken/daklekkage/", "Daklekkage"),
        ("/dakwerken/dakgoot/", "Dakgoot en afvoer"),
        ("/dakwerken/schouw/", "Schouw"),
    ]),
    ("Regels en premies", [
        ("/regelgeving/mijn-verbouwpremie/", "Mijn VerbouwPremie"),
        ("/regelgeving/dakisolatienorm/", "Dakisolatienorm"),
        ("/regelgeving/asbestattest/", "Asbestattest"),
        ("/regelgeving/omgevingsvergunning/", "Omgevingsvergunning"),
        ("/regelgeving/btw-zes-procent/", "Btw 6 procent"),
        ("/regelgeving/epc-renovatieverplichting/", "EPC en renovatieplicht"),
    ]),
    ("Hulpmiddelen", [
        ("/hulpmiddelen/daklekkage-diagnose/", "Daklekkage-diagnose"),
        ("/hulpmiddelen/onderhoudsplanner/", "Onderhoudsplanner"),
        ("/hulpmiddelen/stormschade-en-premiecheck/", "Stormschade en premies"),
        ("/veelgestelde-vragen/", "Veelgestelde vragen"),
        ("/begrippen/", "Begrippenlijst"),
    ]),
    ("Deze site", [
        ("/over/", "Over de gids"),
        ("/contact/", "Contact"),
        ("/nieuws/", "Nieuws"),
        ("/privacybeleid/", "Privacybeleid"),
        ("/cookiebeleid/", "Cookiebeleid"),
    ]),
]

CSS = """
:root{
  --ink:#191817;--ink-2:#403c38;--muted:#6f6a64;
  --line:#e4dfd7;--line-2:#d5cec3;
  --bg:#fbfaf8;--bg-2:#f4f1ec;
  --accent:#9c4a21;--accent-2:#7d3a19;--deep:#20303a;
  --wrap:1180px;--measure:70ch;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,"Times New Roman",serif;
  --sans:"Inter","Segoe UI",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
  font-size:17px;line-height:1.72;-webkit-font-smoothing:antialiased;
  font-variant-numeric:tabular-nums lining-nums}
img{max-width:100%;height:auto}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:2px}
a:hover{color:var(--accent-2)}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 24px}
@media(max-width:600px){.wrap{padding:0 18px}}
.skip{position:absolute;left:-9999px}
.skip:focus{left:10px;top:10px;background:var(--bg);padding:10px 14px;z-index:99;border:1px solid var(--line-2)}

/* ---------- kop ---------- */
header.top{background:var(--bg);border-bottom:1px solid var(--line);
  position:sticky;top:0;z-index:50;backdrop-filter:saturate(140%) blur(6px)}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:20px;
  min-height:62px;padding:8px 0}
.brand{display:flex;flex-direction:column;text-decoration:none;color:var(--ink);line-height:1.25}
.brand b{font-family:var(--serif);font-size:20px;font-weight:600;letter-spacing:-.01em}
.brand span{font-size:11.5px;color:var(--muted);letter-spacing:.05em;text-transform:uppercase}
nav.main ul{list-style:none;display:flex;flex-wrap:wrap;gap:1px;margin:0;padding:0}
nav.main a{display:block;padding:7px 11px;color:var(--ink-2);text-decoration:none;
  font-size:14.5px;border-radius:4px}
nav.main a:hover{color:var(--accent);background:var(--bg-2)}
nav.main a[aria-current]{color:var(--ink);box-shadow:inset 0 -2px 0 var(--accent)}
@media(max-width:900px){
  .topbar{flex-direction:column;align-items:flex-start;gap:6px;padding:12px 0 6px}
  nav.main ul{gap:0;margin-left:-11px}
  nav.main a{padding:6px 11px;font-size:14px}
}

/* ---------- kruimelpad ---------- */
.crumbs{border-bottom:1px solid var(--line);font-size:13px;color:var(--muted)}
.crumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:7px;margin:0;padding:11px 0}
.crumbs a{color:var(--muted);text-decoration:none}
.crumbs a:hover{color:var(--accent)}
.crumbs li:not(:last-child)::after{content:"/";margin-left:7px;color:var(--line-2)}

/* ---------- typografie ---------- */
main{padding:44px 0 20px}
main>.hero:first-child{margin-top:-44px}
h1{font-family:var(--serif);font-weight:600;font-size:clamp(30px,4.6vw,44px);
  line-height:1.12;letter-spacing:-.02em;margin:0 0 18px;max-width:22ch}
h2{font-family:var(--serif);font-weight:600;font-size:clamp(21px,2.5vw,27px);
  line-height:1.25;letter-spacing:-.01em;margin:46px 0 14px}
h3{font-size:17.5px;font-weight:650;letter-spacing:-.005em;margin:30px 0 8px}
p{margin:0 0 17px;max-width:var(--measure)}
.lead{font-size:20px;line-height:1.6;color:var(--ink-2);max-width:60ch;margin-bottom:22px}
ul,ol{margin:0 0 20px;padding-left:20px;max-width:var(--measure)}
li{margin:0 0 9px}
li::marker{color:var(--muted)}
strong,b{font-weight:650}
hr{border:0;border-top:1px solid var(--line);margin:38px 0}

.cols{display:grid;grid-template-columns:minmax(0,1fr) 280px;gap:56px;align-items:start}
@media(max-width:960px){.cols{grid-template-columns:minmax(0,1fr);gap:32px}}
.cols>*{min-width:0}

/* ---------- opener ---------- */
.hero{border-bottom:1px solid var(--line);background:var(--bg);
  padding:70px 0 54px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-40px;bottom:-30px;width:520px;height:230px;
  background-image:
    linear-gradient(45deg,transparent 49.5%,var(--line-2) 49.5%,var(--line-2) 50.5%,transparent 50.5%),
    linear-gradient(-45deg,transparent 49.5%,var(--line-2) 49.5%,var(--line-2) 50.5%,transparent 50.5%);
  background-size:74px 74px;opacity:.5;pointer-events:none}
@media(max-width:820px){.hero::after{display:none}.hero{padding:48px 0 38px}}
.hero .wrap{position:relative;z-index:1}
.hero h1{max-width:17ch;font-size:clamp(32px,5.4vw,52px)}
.hero p{color:var(--ink-2);font-size:19.5px;line-height:1.6;max-width:56ch}
.hero .btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}
.btn{display:inline-block;padding:11px 20px;text-decoration:none;font-weight:600;
  font-size:15px;border-radius:2px;transition:background .15s,color .15s}
.btn.primary{background:var(--accent);color:#fff;border:1px solid var(--accent)}
.btn.primary:hover{background:var(--accent-2);border-color:var(--accent-2);color:#fff}
.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line-2)}
.btn.ghost:hover{border-color:var(--accent);color:var(--accent)}

/* ---------- kerncijfers ---------- */
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
  gap:0;margin:40px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.fact{padding:20px 22px 20px 0;border-right:1px solid var(--line)}
.fact:last-child{border-right:0}
.fact b{display:block;font-family:var(--serif);font-size:31px;font-weight:600;
  line-height:1.1;color:var(--ink);letter-spacing:-.02em}
.fact span{display:block;margin-top:5px;font-size:13.5px;color:var(--muted);line-height:1.45}
@media(max-width:700px){.fact{border-right:0;border-bottom:1px solid var(--line);padding:15px 0}
  .fact:last-child{border-bottom:0}}

/* ---------- tegels ---------- */
.grid{display:grid;gap:0;grid-template-columns:repeat(auto-fill,minmax(268px,1fr));
  margin:22px 0 30px;border-top:1px solid var(--line)}
.tile{display:block;padding:18px 22px 20px 0;text-decoration:none;color:var(--ink);
  border-bottom:1px solid var(--line);position:relative}
.tile::before{content:"";position:absolute;left:0;top:-1px;width:0;height:1px;
  background:var(--accent);transition:width .18s ease}
.tile:hover::before{width:100%}
.tile:hover b{color:var(--accent)}
.tile b{display:block;font-family:var(--serif);font-size:19px;font-weight:600;
  margin-bottom:6px;letter-spacing:-.01em}
.tile span{display:block;font-size:14.5px;color:var(--muted);line-height:1.55;max-width:38ch}

/* ---------- kaders ---------- */
.card{border:1px solid var(--line);padding:20px 22px;margin:0 0 20px;background:var(--bg)}
.card h2,.card h3{margin-top:0}
.card h3{font-family:var(--serif);font-size:16.5px;font-weight:600}

.note{border-left:2px solid var(--accent);padding:4px 0 4px 18px;margin:26px 0;
  font-size:16px;color:var(--ink-2);max-width:var(--measure)}
.note p:last-child{margin-bottom:0}

.rec{border-top:1px solid var(--line-2);border-bottom:1px solid var(--line-2);
  padding:20px 0;margin:38px 0;max-width:var(--measure)}
.rec h3{margin:0 0 8px;font-family:var(--sans);font-size:12px;font-weight:650;
  letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
.rec p{margin:0 0 8px;font-size:16.5px}
.rec p:last-child{margin-bottom:0}
a.ext{color:var(--accent);font-weight:600}
a.ext:hover{color:var(--accent-2)}

/* ---------- tabellen ---------- */
.tablewrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:24px 0 28px}
table{width:100%;border-collapse:collapse;font-size:15.5px;min-width:420px}
th,td{text-align:left;padding:11px 16px 11px 0;border-bottom:1px solid var(--line);
  vertical-align:top;line-height:1.55}
th{font-size:12px;font-weight:650;letter-spacing:.07em;text-transform:uppercase;
  color:var(--muted);border-bottom:1px solid var(--line-2);padding-bottom:9px}
tr:last-child td{border-bottom:1px solid var(--line-2)}

/* ---------- overig ---------- */
.small{font-size:14px;color:var(--muted)}
.src{font-size:14px;color:var(--muted);overflow-wrap:anywhere;list-style:none;padding-left:0}
.src li{margin-bottom:8px;padding-left:14px;position:relative}
.src li::before{content:"";position:absolute;left:0;top:11px;width:6px;height:1px;background:var(--line-2)}

.chips{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:0 0 26px;max-width:none}
.chips a{display:inline-block;padding:5px 12px;border:1px solid var(--line);
  font-size:14px;text-decoration:none;color:var(--ink-2);border-radius:2px}
.chips a:hover{border-color:var(--accent);color:var(--accent)}

/* ---------- hulpmiddelen ---------- */
.tool{border:1px solid var(--line);padding:26px;background:var(--bg);margin:0 0 26px}
.tool fieldset{border:0;padding:0;margin:0 0 24px}
.tool legend{font-family:var(--serif);font-weight:600;font-size:17px;padding:0;margin-bottom:11px}
.opt{display:block;border:1px solid var(--line);padding:11px 14px;margin-bottom:7px;
  cursor:pointer;font-size:15.5px;border-radius:2px;transition:border-color .12s,background .12s}
.opt:hover{border-color:var(--line-2);background:var(--bg-2)}
.opt:has(input:checked){border-color:var(--accent);background:var(--bg-2)}
.opt input{margin-right:10px;accent-color:var(--accent)}
.tool select,.tool input[type=number],.tool input[type=text]{
  width:100%;max-width:360px;padding:10px 12px;border:1px solid var(--line-2);
  font-size:15.5px;background:var(--bg);color:var(--ink);border-radius:2px;font-family:inherit}
.tool select:focus,.tool input:focus{outline:2px solid var(--accent);outline-offset:1px}
.tool label.field{display:block;margin-bottom:18px;font-size:15px}
.tool label.field b{display:block;font-weight:650;margin-bottom:6px}
.result{border-top:2px solid var(--accent);background:var(--bg-2);padding:20px 22px;margin-top:22px}
.result h3{margin-top:0}
.result p,.result ul,.result ol{max-width:none}
.verdict{font-family:var(--serif);font-size:20px;font-weight:600;color:var(--ink);margin-bottom:10px}
.bar{height:4px;background:var(--line);overflow:hidden;margin:9px 0 5px;max-width:340px}
.bar i{display:block;height:100%;background:var(--accent)}
.tag{display:inline-block;font-size:12px;letter-spacing:.06em;text-transform:uppercase;
  font-weight:650;padding:3px 9px;border:1px solid var(--line-2);color:var(--ink-2);margin-right:7px}
.tag.hi{border-color:var(--accent);color:var(--accent)}
.tag.ok{border-color:var(--line-2);color:var(--muted)}

/* ---------- nieuws ---------- */
article.news h2{margin-top:38px}
.meta{font-size:13px;color:var(--muted);letter-spacing:.04em;text-transform:uppercase;
  margin:-8px 0 20px}
.newslist{list-style:none;padding:0;margin:0;border-top:1px solid var(--line)}
.newslist li{border-bottom:1px solid var(--line);padding:22px 0;max-width:none}
.newslist a{font-family:var(--serif);font-size:21px;font-weight:600;text-decoration:none;
  color:var(--ink);letter-spacing:-.01em;line-height:1.3;display:inline-block}
.newslist a:hover{color:var(--accent)}
.newslist .meta{margin:7px 0 6px}
.newslist p{margin:0;color:var(--ink-2);font-size:16px;max-width:62ch}

/* ---------- zijkolom ---------- */
aside .card{position:sticky;top:86px;border:0;border-top:2px solid var(--ink);
  padding:16px 0 0;background:transparent}
aside .card h3{font-family:var(--sans);font-size:12px;font-weight:650;letter-spacing:.09em;
  text-transform:uppercase;color:var(--muted);margin-bottom:12px}
aside ul{font-size:15px;padding-left:0;list-style:none}
aside ul li{margin-bottom:8px}
aside a{color:var(--ink-2);text-decoration:none}
aside a:hover{color:var(--accent)}
aside .chips a{color:var(--ink-2)}

/* ---------- voet ---------- */
footer.bot{border-top:1px solid var(--line);margin-top:70px;padding:44px 0 30px;
  font-size:14.5px;color:var(--muted);background:var(--bg-2)}
footer.bot h4{font-size:12px;font-weight:650;letter-spacing:.09em;text-transform:uppercase;
  color:var(--ink-2);margin:0 0 12px}
footer.bot ul{list-style:none;padding:0;margin:0;max-width:none}
footer.bot li{margin-bottom:8px}
footer.bot a{color:var(--muted);text-decoration:none}
footer.bot a:hover{color:var(--accent)}
.fcols{display:grid;gap:32px;grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}
.fbottom{border-top:1px solid var(--line);margin-top:34px;padding-top:20px;display:flex;
  flex-wrap:wrap;gap:14px;justify-content:space-between;font-size:13.5px}
"""

CSS_DARK = """
@media (prefers-color-scheme: dark){
  :root{--ink:#eae7e1;--ink-2:#c6c1b9;--muted:#948e86;
    --line:#2e302d;--line-2:#3a3d39;
    --bg:#141513;--bg-2:#1c1e1c;
    --accent:#d8834f;--accent-2:#e79c6b;--deep:#c9d3d8;}
  .btn.primary{color:#14140f}
  .btn.primary:hover{color:#14140f}
  aside .card{border-top-color:var(--ink-2)}
  .skip{background:var(--bg-2)}
}
"""


def slug(s):
    s = s.lower()
    for a, b in (("á","a"),("à","a"),("ä","a"),("â","a"),("é","e"),("è","e"),("ë","e"),
                 ("ê","e"),("í","i"),("ï","i"),("ó","o"),("ö","o"),("ô","o"),("ú","u"),
                 ("ü","u"),("û","u"),("ç","c"),("'","-"),("’","-")):
        s = s.replace(a, b)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def esc(s):
    return html.escape(s, quote=False)


class Page:
    def __init__(self, path, title, description, body, crumbs=None, aside=None,
                 changefreq="monthly", priority="0.6", schema=None, date=None,
                 head_extra="", noindex=False):
        self.path = path
        self.title = title
        self.description = description
        self.body = body
        self.crumbs = crumbs or []
        self.aside = aside
        self.changefreq = changefreq
        self.priority = priority
        self.schema = schema
        self.date = date
        self.head_extra = head_extra
        self.noindex = noindex


def add(page):
    PAGES.append(page)
    return page


def nav_html(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current or (
            href != "/" and current.startswith(href)) else ""
        items.append('<li><a href="%s"%s>%s</a></li>' % (href, cur, label))
    return "<ul>%s</ul>" % "".join(items)


def crumbs_html(crumbs, title):
    if not crumbs:
        return ""
    parts = ['<li><a href="/">Home</a></li>']
    for href, label in crumbs:
        parts.append('<li><a href="%s">%s</a></li>' % (href, esc(label)))
    parts.append("<li>%s</li>" % esc(title))
    return ('<div class="crumbs"><div class="wrap"><nav aria-label="Kruimelpad">'
            '<ol>%s</ol></nav></div></div>' % "".join(parts))


def footer_html():
    cols = []
    for head, links in FOOTER_COLS:
        li = "".join('<li><a href="%s">%s</a></li>' % (h, esc(l)) for h, l in links)
        cols.append("<div><h4>%s</h4><ul>%s</ul></div>" % (esc(head), li))
    year = datetime.date.today().year
    return ('<footer class="bot"><div class="wrap"><div class="fcols">%s</div>'
            '<div class="fbottom"><span>&copy; %d %s. Redactionele gids, geen dakwerkenbedrijf.</span>'
            '<span>Contact: <a href="mailto:%s">%s</a></span></div></div></footer>'
            % ("".join(cols), year, SITE_NAME, EMAIL, EMAIL))


TEMPLATE = """<!doctype html>
<html lang="{locale}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{robots}<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{site}">
<meta property="og:locale" content="nl_BE">
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="{site} nieuws" href="/rss.xml">
{schema}{head_extra}</head>
<body>
<a class="skip" href="#main">Naar de inhoud</a>
<header class="top"><div class="wrap"><div class="topbar">
<a class="brand" href="/"><b>{site}</b><span>{tagline}</span></a>
<nav class="main" aria-label="Hoofdmenu">{nav}</nav>
</div></div></header>
{crumbs}
<main id="main">{body}</main>
{footer}
</body>
</html>
"""


def seo_title(t):
    """Merkachtervoegsel toevoegen zolang de title binnen 62 tekens blijft."""
    suffix = " | " + SITE_NAME
    if len(t) + len(suffix) <= 62:
        return t + suffix
    return t


def render(page):
    schema = ""
    if page.schema:
        import json
        schema = ('<script type="application/ld+json">%s</script>\n'
                  % json.dumps(page.schema, ensure_ascii=False))
    canonical = BASE + page.path
    return TEMPLATE.format(
        locale=LOCALE,
        title=esc(seo_title(page.title)),
        description=esc(page.description),
        canonical=canonical,
        robots='<meta name="robots" content="noindex,follow">\n' if page.noindex else "",
        ogtype="article" if page.date else "website",
        site=SITE_NAME,
        tagline=TAGLINE,
        schema=schema,
        head_extra=page.head_extra,
        nav=nav_html(page.path),
        crumbs=crumbs_html(page.crumbs, page.title),
        body=page.body,
        footer=footer_html(),
    )


def write(dist="dist"):
    for p in PAGES:
        rel = p.path.lstrip("/")
        out = os.path.join(dist, rel, "index.html") if not rel.endswith(".html") \
            else os.path.join(dist, rel)
        if p.path == "/":
            out = os.path.join(dist, "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(render(p))
    os.makedirs(os.path.join(dist, "assets"), exist_ok=True)
    with open(os.path.join(dist, "assets", "site.css"), "w", encoding="utf-8") as f:
        f.write(CSS.rstrip() + "\n" + CSS_DARK)
