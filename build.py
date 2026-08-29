# -*- coding: utf-8 -*-
import os, shutil, datetime
import engine
from engine import PAGES, BASE, SITE_NAME, EMAIL
import pages_gids, pages_regels, pages_tools, pages_locaties, pages_nieuws, pages_misc

DIST = "dist"

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="12" fill="#1d3f5c"/>
<path d="M8 34 32 14l24 20v3h-6L32 22 14 37H8z" fill="#b4531f"/>
<path d="M14 37h36v15a3 3 0 0 1-3 3H17a3 3 0 0 1-3-3z" fill="#f2f5f8"/>
<rect x="27" y="42" width="10" height="13" fill="#1d3f5c"/>
</svg>"""

HEADERS = """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), camera=(), microphone=(), interest-cohort=()
/assets/*
  Cache-Control: public, max-age=31536000, immutable
"""


def sitemap():
    today = datetime.date.today().isoformat()
    urls = []
    for p in sorted(PAGES, key=lambda x: x.path):
        if p.noindex:
            continue
        urls.append("<url><loc>%s%s</loc><lastmod>%s</lastmod>"
                    "<changefreq>%s</changefreq><priority>%s</priority></url>"
                    % (BASE, p.path, p.date or today, p.changefreq, p.priority))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>'
            % "".join(urls))


def robots():
    return ("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)


def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    pages_misc_last = pages_misc  # home heeft de nieuwslijst nodig
    pages_gids.build()
    pages_regels.build()
    pages_tools.build()
    pages_locaties.build()
    pages_nieuws.build()
    pages_misc_last.build()

    engine.write(DIST)

    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap())
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots())
    with open(os.path.join(DIST, "rss.xml"), "w", encoding="utf-8") as f:
        f.write(pages_nieuws.rss())
    with open(os.path.join(DIST, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON)
    with open(os.path.join(DIST, "_headers"), "w", encoding="utf-8") as f:
        f.write(HEADERS)

    n = sum(len(files) for _, _, files in os.walk(DIST))
    print("Pagina's: %d, bestanden in dist: %d" % (len(PAGES), n))


if __name__ == "__main__":
    main()
