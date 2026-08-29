# vencodakwerken.be

Generator voor de statische site op https://vencodakwerken.be/

Onafhankelijke dakwerkengids voor Vlaanderen. De site promoot Den Dekker Dakbedekking
en linkt naar de gemeentepagina's van dat bedrijf in de provincies Antwerpen en Limburg.

## Bouwen

    python3 build.py    # schrijft dist/
    python3 check.py    # controleert de gebouwde site

Geen dependencies. `build.py` schrijft 79 pagina's plus sitemap.xml, robots.txt,
rss.xml, favicon.svg en _headers naar `dist/`.

## Bestanden

| Bestand | Inhoud |
| --- | --- |
| `engine.py` | sjabloon, navigatie, CSS, sitemapgegevens |
| `data_gemeenten.py` | 38 Vlaamse gemeenten met streek, deelkernen en profiel |
| `pages_gids.py` | twaalf hoofdstukken over dakonderdelen |
| `pages_regels.py` | zes Vlaamse regelingen en premies |
| `pages_tools.py` | daklekkage-diagnose, onderhoudsplanner, storm- en premiecheck |
| `pages_locaties.py` | locatie-index en gemeentepagina's |
| `pages_nieuws.py` | nieuwsartikelen en RSS |
| `pages_misc.py` | home, over, faq, begrippen, contact, privacy, cookies, 404 |
| `check.py` | controle op kapotte links, dubbele meta, aanspreekvormen, ankerteksten |

## Publicatie

Cloudflare Pages, directe upload van een zip met de inhoud van `dist/` in de zipwortel.
