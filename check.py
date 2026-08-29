# -*- coding: utf-8 -*-
"""Controleert de gebouwde site op fouten die een bezoeker of zoekmachine zou zien."""
import os, re, sys, collections

DIST = "dist"
ALLOWED_HOSTS = {"www.dendekker-dakbedekking.nl"}
ALLOWED_ANCHOR_PREFIX = ("Den Dekker Dakbedekking", "dendekker-dakbedekking.nl",
                         "https://www.dendekker-dakbedekking.nl")
# aanspreekvormen en wij-vorm, als heel woord
FORBIDDEN_WORDS = ["je", "jij", "jou", "jouw", "jullie", "uw", "we", "wij", "ons", "onze"]
DUMMY = ["lorem ipsum", "todo", "tbd", "xxx", "placeholder", "voorbeeldtekst",
         "vul hier", "nog invullen", "dummy"]

errors = []
warns = []


def err(f, m):
    errors.append("%s: %s" % (f, m))


def warn(f, m):
    warns.append("%s: %s" % (f, m))


def strip_tags(html):
    html = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    html = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    html = html.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", html)


def main():
    files = []
    for root, _, fs in os.walk(DIST):
        for f in fs:
            if f.endswith(".html"):
                files.append(os.path.join(root, f))
    if not files:
        print("Geen html gevonden. Eerst build.py draaien.")
        sys.exit(1)

    paths = set()
    for f in files:
        rel = os.path.relpath(f, DIST)
        if rel == "index.html":
            paths.add("/")
        elif rel.endswith("/index.html"):
            paths.add("/" + rel[:-len("index.html")])
        else:
            paths.add("/" + rel)

    titles = collections.Counter()
    descs = collections.Counter()
    linked = set()

    for f in sorted(files):
        html = open(f, encoding="utf-8").read()
        rel = "/" + os.path.relpath(f, DIST)
        text = strip_tags(html)

        # meta
        t = re.search(r"<title>(.*?)</title>", html, re.S)
        d = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
        if not t:
            err(rel, "geen title")
        else:
            tt = t.group(1).strip()
            titles[tt] += 1
            if len(tt) > 65:
                warn(rel, "title %d tekens: %s" % (len(tt), tt))
            if len(tt) < 15:
                warn(rel, "title erg kort: %s" % tt)
        if not d:
            err(rel, "geen meta description")
        else:
            dd = d.group(1).strip()
            descs[dd] += 1
            if not (60 <= len(dd) <= 185):
                warn(rel, "description %d tekens" % len(dd))

        if 'rel="canonical"' not in html:
            err(rel, "geen canonical")

        h1 = re.findall(r"<h1[^>]*>", html)
        if len(h1) != 1:
            err(rel, "%d h1-tags" % len(h1))

        # em-dash en en-dash
        for ch, naam in (("—", "em-dash"), ("–", "en-dash")):
            if ch in html:
                err(rel, "bevat %s" % naam)

        # dummytekst
        low = text.lower()
        for dmy in DUMMY:
            if dmy in low:
                err(rel, "dummytekst '%s'" % dmy)

        # aanspreekvormen in de zichtbare tekst
        for w in FORBIDDEN_WORDS:
            for m in re.finditer(r"(?<![\w-])%s(?![\w-])" % re.escape(w), text, re.I):
                ctx = text[max(0, m.start() - 45):m.end() + 45]
                err(rel, "aanspreekvorm of wij-vorm '%s': ...%s..." % (w, ctx.strip()))
                break

        # interne links
        for href in re.findall(r'href="(/[^"#]*)"', html):
            href = href.split("?")[0]
            linked.add(href)
            if href.endswith((".xml", ".txt", ".svg", ".css")):
                if not os.path.exists(os.path.join(DIST, href.lstrip("/"))):
                    err(rel, "kapotte link naar bestand %s" % href)
                continue
            if href not in paths:
                err(rel, "kapotte interne link %s" % href)

        # uitgaande links
        for m in re.finditer(r'<a\s([^>]*)href="(https?://[^"]+)"([^>]*)>(.*?)</a>',
                             html, re.S | re.I):
            attrs = m.group(1) + m.group(3)
            url = m.group(2)
            anchor = strip_tags(m.group(4)).strip()
            host = url.split("/")[2]
            if host not in ALLOWED_HOSTS:
                err(rel, "uitgaande link naar niet-toegestane host %s" % host)
            if "nofollow" not in attrs or "noopener" not in attrs:
                err(rel, "uitgaande link zonder nofollow noopener: %s" % url)
            if not anchor.startswith(ALLOWED_ANCHOR_PREFIX):
                err(rel, "ankertekst niet toegestaan: '%s'" % anchor)

        # lege links
        for m in re.finditer(r'<a\s[^>]*>(\s*)</a>', html):
            err(rel, "lege link")

        # afbeeldingen zonder alt
        for m in re.finditer(r"<img\s([^>]*)>", html):
            if "alt=" not in m.group(1):
                err(rel, "img zonder alt")

        # dubbele id
        ids = re.findall(r'\sid="([^"]+)"', html)
        for i, c in collections.Counter(ids).items():
            if c > 1:
                err(rel, "dubbel id '%s'" % i)

    for t, c in titles.items():
        if c > 1:
            err("(algemeen)", "dubbele title %dx: %s" % (c, t))
    for d, c in descs.items():
        if c > 1:
            err("(algemeen)", "dubbele description %dx: %s" % (c, d[:70]))

    # sitemap dekking
    sm = open(os.path.join(DIST, "sitemap.xml"), encoding="utf-8").read()
    in_sm = set(re.findall(r"<loc>https?://[^/]+([^<]*)</loc>", sm))
    for p in paths:
        if p == "/404.html":
            continue
        if p not in in_sm:
            err("sitemap.xml", "ontbreekt: %s" % p)
    for p in in_sm:
        if p not in paths:
            err("sitemap.xml", "verwijst naar onbestaande pagina: %s" % p)

    # verweesde pagina's
    for p in sorted(paths):
        if p in ("/", "/404.html"):
            continue
        if p not in linked:
            warn("(algemeen)", "geen enkele interne link naar %s" % p)

    print("Pagina's gecontroleerd: %d" % len(files))
    if warns:
        print("\nWaarschuwingen (%d):" % len(warns))
        for w in warns[:60]:
            print("  " + w)
        if len(warns) > 60:
            print("  ... en nog %d" % (len(warns) - 60))
    if errors:
        print("\nFOUTEN (%d):" % len(errors))
        for e in errors[:120]:
            print("  " + e)
        if len(errors) > 120:
            print("  ... en nog %d" % (len(errors) - 120))
        sys.exit(1)
    print("\nGeen fouten.")


if __name__ == "__main__":
    main()
