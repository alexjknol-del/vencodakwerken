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
  --ink:#161a1d;--ink-2:#3d474e;--muted:#66727b;--line:#dfe4e8;
  --bg:#ffffff;--bg-2:#f4f6f8;--bg-3:#eceff2;
  --brand:#1d3f5c;--brand-2:#2b5c85;--accent:#b4531f;--accent-2:#8f4018;
  --ok:#1f6b45;--warn:#8a5a08;--radius:10px;--wrap:1120px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.65 "Inter","Segoe UI",system-ui,-apple-system,Arial,sans-serif}
img{max-width:100%;height:auto}
a{color:var(--brand-2)}
a:hover{color:var(--accent-2)}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 20px}
.skip{position:absolute;left:-9999px}
.skip:focus{left:8px;top:8px;background:#fff;padding:8px 12px;z-index:99}

header.top{background:var(--brand);color:#fff}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:14px 0}
.brand{display:flex;flex-direction:column;text-decoration:none;color:#fff}
.brand b{font-size:19px;letter-spacing:.2px}
.brand span{font-size:12.5px;color:#bcd0e0}
nav.main ul{list-style:none;display:flex;flex-wrap:wrap;gap:2px;margin:0;padding:0}
nav.main a{display:block;padding:8px 11px;color:#dce8f2;text-decoration:none;
  border-radius:7px;font-size:14.5px}
nav.main a:hover{background:var(--brand-2);color:#fff}
nav.main a[aria-current]{background:var(--brand-2);color:#fff}
@media(max-width:820px){.topbar{flex-direction:column;align-items:flex-start;gap:10px}
  nav.main ul{gap:4px}
  nav.main a{padding:7px 9px;font-size:14px}}

.crumbs{background:var(--bg-2);border-bottom:1px solid var(--line);font-size:13.5px;color:var(--muted)}
.crumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:6px;margin:0;padding:9px 0}
.crumbs li:not(:last-child)::after{content:"/";margin-left:6px;color:#9aa5ad}

main{padding:34px 0 10px}
main>.hero:first-child{margin-top:-34px}
h1{font-size:clamp(26px,4vw,36px);line-height:1.2;margin:0 0 14px;letter-spacing:-.4px}
h2{font-size:clamp(20px,2.6vw,25px);line-height:1.3;margin:34px 0 12px;letter-spacing:-.2px}
h3{font-size:18px;margin:24px 0 8px}
p{margin:0 0 14px}
.lead{font-size:18px;color:var(--ink-2)}
ul,ol{margin:0 0 16px;padding-left:22px}
li{margin:0 0 7px}
.cols{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:36px;align-items:start}
@media(max-width:900px){.cols{grid-template-columns:minmax(0,1fr)}}
.cols>*{min-width:0}

.card{background:var(--bg-2);border:1px solid var(--line);border-radius:var(--radius);padding:18px 20px;margin:0 0 18px}
.card h2,.card h3{margin-top:0}
.card.accent{background:#fdf4ee;border-color:#f0d6c4}
.card.quiet{background:#fff}

.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));margin:0 0 22px}
.tile{display:block;background:var(--bg-2);border:1px solid var(--line);border-radius:var(--radius);
  padding:16px 18px;text-decoration:none;color:var(--ink)}
.tile:hover{border-color:var(--brand-2);background:#fff}
.tile b{display:block;font-size:16.5px;margin-bottom:5px;color:var(--brand)}
.tile span{font-size:14px;color:var(--muted);line-height:1.5}

.hero{background:linear-gradient(180deg,var(--brand) 0%,#17334a 100%);color:#fff;padding:52px 0 46px}
.hero h1{color:#fff;max-width:22ch}
.hero p{color:#c9d9e6;font-size:18px;max-width:62ch}
.hero .btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
.btn{display:inline-block;padding:11px 18px;border-radius:8px;text-decoration:none;font-weight:600;font-size:15px}
.btn.primary{background:var(--accent);color:#fff}
.btn.primary:hover{background:var(--accent-2);color:#fff}
.btn.ghost{background:rgba(255,255,255,.10);color:#fff;border:1px solid rgba(255,255,255,.35)}
.btn.ghost:hover{background:rgba(255,255,255,.2);color:#fff}

.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px;margin:26px 0}
.fact{background:var(--bg-2);border:1px solid var(--line);border-radius:var(--radius);padding:14px 16px}
.fact b{display:block;font-size:23px;color:var(--brand);line-height:1.2}
.fact span{font-size:13.5px;color:var(--muted)}

table{width:100%;border-collapse:collapse;margin:0 0 18px;font-size:15px}
.tablewrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:0 0 18px}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--bg-3);font-size:14px}

.rec{border:1px solid #f0d6c4;background:#fdf4ee;border-radius:var(--radius);padding:18px 20px;margin:26px 0}
.rec h2,.rec h3{margin-top:0;color:var(--accent-2)}
.rec .ext{font-weight:600}
a.ext{color:var(--accent-2)}

.note{border-left:3px solid var(--brand-2);background:var(--bg-2);padding:12px 16px;margin:0 0 18px;font-size:15px}
.small{font-size:13.5px;color:var(--muted)}
.src{font-size:13.5px;color:var(--muted);overflow-wrap:anywhere}
.src li{margin-bottom:5px}

.chips{display:flex;flex-wrap:wrap;gap:7px;list-style:none;padding:0;margin:0 0 20px}
.chips a{display:inline-block;padding:6px 11px;background:var(--bg-2);border:1px solid var(--line);
  border-radius:99px;font-size:14px;text-decoration:none;color:var(--ink-2)}
.chips a:hover{border-color:var(--brand-2);color:var(--brand)}

.tool{border:1px solid var(--line);border-radius:var(--radius);padding:20px;background:#fff;margin:0 0 22px}
.tool fieldset{border:0;padding:0;margin:0 0 18px}
.tool legend{font-weight:600;font-size:16px;padding:0;margin-bottom:9px}
.opt{display:block;border:1px solid var(--line);border-radius:8px;padding:10px 13px;margin-bottom:8px;cursor:pointer;font-size:15px}
.opt:hover{border-color:var(--brand-2);background:var(--bg-2)}
.opt input{margin-right:9px}
.tool select,.tool input[type=number],.tool input[type=text]{
  width:100%;max-width:340px;padding:9px 11px;border:1px solid var(--line);border-radius:8px;font-size:15px;background:#fff;color:var(--ink)}
.tool label.field{display:block;margin-bottom:14px;font-size:15px}
.tool label.field b{display:block;font-weight:600;margin-bottom:5px}
.result{border:1px solid var(--line);border-radius:var(--radius);background:var(--bg-2);padding:16px 18px;margin-top:16px}
.result h3{margin-top:0}
.result .verdict{font-size:17px;font-weight:600;color:var(--brand)}
.bar{height:9px;background:var(--bg-3);border-radius:99px;overflow:hidden;margin:8px 0 4px}
.bar i{display:block;height:100%;background:var(--brand-2)}
.tag{display:inline-block;font-size:12.5px;padding:3px 9px;border-radius:99px;background:var(--bg-3);color:var(--ink-2);margin-right:6px}
.tag.hi{background:#f7e0d5;color:var(--accent-2)}
.tag.ok{background:#dff0e6;color:var(--ok)}

article.news h2{margin-top:30px}
.meta{font-size:13.5px;color:var(--muted);margin:-6px 0 18px}
.newslist{list-style:none;padding:0;margin:0}
.newslist li{border-bottom:1px solid var(--line);padding:16px 0}
.newslist a{font-size:17.5px;font-weight:600;text-decoration:none}
.newslist p{margin:5px 0 0;color:var(--ink-2);font-size:15px}

aside .card{position:sticky;top:16px}
footer.bot{background:#12212e;color:#a9bcca;margin-top:44px;padding:34px 0 22px;font-size:14.5px}
footer.bot h4{color:#fff;font-size:14px;text-transform:none;margin:0 0 10px;letter-spacing:.3px}
footer.bot ul{list-style:none;padding:0;margin:0}
footer.bot li{margin-bottom:6px}
footer.bot a{color:#a9bcca;text-decoration:none}
footer.bot a:hover{color:#fff}
.fcols{display:grid;gap:26px;grid-template-columns:repeat(auto-fit,minmax(190px,1fr))}
.fbottom{border-top:1px solid #23384a;margin-top:26px;padding-top:16px;display:flex;
  flex-wrap:wrap;gap:12px;justify-content:space-between;font-size:13.5px}
"""

CSS_DARK = """
@media (prefers-color-scheme: dark){
  :root{--ink:#e9edf1;--ink-2:#c3ccd4;--muted:#94a2ad;--line:#2a3540;
    --bg:#11171d;--bg-2:#182029;--bg-3:#1f2933;
    --brand:#12293b;--brand-2:#79b0d8;--accent:#d97a3e;--accent-2:#e8925a;}
  .card.accent,.rec{background:#241a13;border-color:#4a3423}
  .tile:hover{background:var(--bg-3)}
  .tool,.card.quiet{background:var(--bg-2)}
  .tool select,.tool input{background:var(--bg-3);color:var(--ink);border-color:var(--line)}
  .hero{background:linear-gradient(180deg,#152b3d 0%,#101c27 100%)}
  footer.bot{background:#0d141a}
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
