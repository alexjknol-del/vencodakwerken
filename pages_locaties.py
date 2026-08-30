# -*- coding: utf-8 -*-
"""Locatiepagina's per gemeente."""
from engine import Page, add, dd_link, dd_url
from data_gemeenten import GEMEENTEN

CR = [("/locaties/", "Locaties")]

STREEK_TEKST = {
    "Stad Antwerpen": (
        "In de stad staat de bebouwing dicht op elkaar. Dakwerken gebeuren er bijna altijd met "
        "medewerking van de buren, omdat de stelling op het voetpad of tegen de scheidingsmuur komt. "
        "Voor een deel van de wijken gelden bovendien beschermde stads- of dorpsgezichten en "
        "erfgoedregels die de vrijstelling van omgevingsvergunning doorkruisen."),
    "Antwerpse rand": (
        "De randgemeenten kennen veel open en halfopen bebouwing uit de periode 1930 tot 1980, met "
        "grote dakvlakken en volgroeide tuinen. Bomen dicht bij de woning betekenen meer blad in de "
        "goot en meer mosgroei op de noordzijde van het dak."),
    "Antwerpse Polder": (
        "In de polder is de bebouwing open en staat weinig in de luwte. Dat verhoogt de belasting op "
        "nokvorsten, gevelpannen en dakranden, precies de onderdelen die bij storm het eerst loskomen."),
    "Noorderkempen": (
        "De Noorderkempen zijn landelijk, met veel losse hoeves, schuren en loodsen naast de woningen. "
        "Op die bijgebouwen ligt vaak nog asbestcement in golfplaatvorm, wat de werkwijze en de "
        "afvoer bij een dakvernieuwing bepaalt."),
    "Kempen": (
        "De Kempen tellen veel vrijstaande woningen uit de periode 1960 tot 1985 op ruime percelen. "
        "Bij die generatie woningen is de eerste dakbedekking nu aan het einde van haar levensduur en "
        "ontbreekt de dakisolatie vaak of ligt ze alleen tussen de kepers zonder onderdak."),
    "Voorkempen": (
        "In de Voorkempen wisselen oudere dorpskernen af met naoorlogse verkavelingen en bosrijke "
        "wijken. Bungalows met een flauwe dakhelling komen er veel voor, een dakvorm die gevoelig is "
        "voor inwaaiende regen onder de pannen."),
    "Zuiderkempen": (
        "De Zuiderkempen combineren compacte dorpskernen met lintbebouwing langs de invalswegen. In de "
        "kernen gaat het om gesloten bebouwing met hellende daken vooraan en platte aanbouwen achteraan."),
    "Noord-Limburg": (
        "Noord-Limburg heeft een gespreide bebouwing op zandgrond, met kernen die soms kilometers uit "
        "elkaar liggen. Veel woningen dateren uit de jaren zestig tot tachtig, waardoor dakvernieuwing "
        "en isolatie er vaak samenvallen."),
    "Maasland": (
        "Het Maasland ligt in het dal van de Maas. De open ligging betekent weinig beschutting tegen "
        "wind op de dakranden, en in de historische kernen gelden erfgoedregels bij het wijzigen van "
        "dakvorm of dakbedekking."),
}


def build():
    prov = {}
    for g in GEMEENTEN:
        prov.setdefault(g[2], []).append(g)
    blocks = []
    for p in ("Antwerpen", "Limburg"):
        items = sorted(prov[p], key=lambda x: x[1])
        chips = "".join('<li><a href="/locaties/%s/">%s</a></li>' % (g[0], g[1]) for g in items)
        blocks.append("<h2>Provincie %s, %d gemeenten</h2><ul class=\"chips\">%s</ul>" % (p, len(items), chips))

    add(Page("/locaties/", "Dakwerken per gemeente in Vlaanderen",
             "Overzicht van de Vlaamse gemeenten in de provincies Antwerpen en Limburg met een eigen pagina over dakwerken, de plaatselijke bebouwing en de aanbevolen uitvoerder.",
             """<div class="wrap">
<h1>Dakwerken per gemeente</h1>
<p class="lead">Achtendertig gemeenten in de provincies Antwerpen en Limburg hebben een eigen pagina. Elke pagina beschrijft de kernen, de bebouwing en de dakvraagstukken die er het meest spelen, en verwijst naar de plaatselijke pagina van de aanbevolen uitvoerder.</p>
%s
<h2>Waarom de gemeente uitmaakt</h2>
<p>Bebouwing verschilt per streek, en daarmee ook de dakvraagstukken. In de Kempen gaat het vaak om vrijstaande woningen uit de jaren zestig en zeventig waarvan de eerste dakbedekking op is. In de stad om rijwoningen waarbij het hellende voordak en het platte achterdak op elkaar aansluiten. In de polder en het Maasland om windbelasting op open liggingen. En in de gebieden rond de Kolonies van Wortel en Merksplas om erfgoedregels die de vrijstelling van omgevingsvergunning doorkruisen.</p>
<div class="rec"><h3>Uitvoering</h3>
<p>Aanbevolen uitvoerder voor de gemeenten in deze lijst: %s, 085 130 2723.</p>
<p>Overzicht van alle werkgebieden: %s</p></div>
</div>""" % ("".join(blocks), dd_link(), dd_link("locaties/", "dendekker-dakbedekking.nl/locaties/")),
             priority="0.8"))

    for g in GEMEENTEN:
        _gemeente(g)


def _gemeente(g):
    slug, naam, provincie, streek, kernen, profiel = g
    buren = [x for x in GEMEENTEN if x[3] == streek and x[0] != slug][:6]
    burenhtml = "".join('<li><a href="/locaties/%s/">%s</a></li>' % (b[0], b[1]) for b in buren)
    streektekst = STREEK_TEKST.get(streek, "")
    limburg = provincie == "Limburg"

    aside = ('<aside><div class="card"><h3>Gemeenten in %s</h3><ul class="chips">%s</ul>'
             '<p class="small"><a href="/locaties/">Alle gemeenten</a></p></div></aside>'
             % (streek, burenhtml or '<li><a href="/locaties/">Alle gemeenten</a></li>'))

    body = """<h1>Dakwerken in %(naam)s</h1>
<p class="lead">%(naam)s ligt in de provincie %(prov)s, in de streek %(streek)s. De gemeente omvat %(kernen)s.</p>

<h2>De bebouwing in %(naam)s</h2>
<p>%(profiel)s</p>
<p>%(streektekst)s</p>

<h2>Wat er in %(naam)s het vaakst speelt</h2>
<ul>
<li><b>Daklekkage.</b> De instroomplek ligt zelden recht boven de vlek. De <a href="/hulpmiddelen/daklekkage-diagnose/">daklekkage-diagnose</a> zet de meest waarschijnlijke oorzaken op een rij op basis van symptomen.</li>
<li><b>Nokvorsten en gevelpannen.</b> Mortel onder de nok scheurt door vorst en temperatuurwisselingen. Zie <a href="/dakwerken/hellend-dak/">hellend dak</a>.</li>
<li><b>Goten.</b> Bladophoping bij de tapbuis is de meest voorkomende oorzaak van een overlopende goot. Zie <a href="/dakwerken/dakgoot/">dakgoot en regenafvoer</a>.</li>
<li><b>Dakisolatie.</b> De Vlaamse norm ligt op R 0,75, de premievoorwaarde op Rd 4,5. Zie <a href="/regelgeving/dakisolatienorm/">de dakisolatienorm</a>.</li>
<li><b>Asbest.</b> Bij gebouwen van voor 2001 is asbestcement op daken en bijgebouwen niet uitgesloten. Zie <a href="/dakwerken/asbest-op-het-dak/">asbest op het dak</a>.</li>
</ul>

<h2>Regels en premies in %(naam)s</h2>
<p>Voor %(naam)s gelden dezelfde Vlaamse regels als in de rest van het gewest. Het vervangen van dakbedekking zonder wijziging van het bouwvolume is vrijgesteld van omgevingsvergunning; buitenisolatie tot 26 centimeter eveneens. Die vrijstelling vervalt bij panden op de vastgestelde inventaris van het bouwkundig erfgoed en in werelderfgoedgebieden en hun bufferzones. Gemeentelijke plannen en verkavelingsvoorschriften kunnen strenger zijn, dus navraag bij de gemeente %(naam)s blijft de eerste stap.</p>
<p>Mijn VerbouwPremie voor het dak bedraagt voor categorie 4 50 procent van de investering exclusief btw met een maximum van 5.750 euro, en voor categorie 3 35 procent met een maximum van 4.025 euro. Voor de categorieen 1 en 2 en voor niet-bewonende investeerders vervalt de premie op 1 maart 2026. De <a href="/hulpmiddelen/stormschade-en-premiecheck/">premiecheck</a> rekent dat door. %(limburgzin)s</p>

<div class="rec"><h3>Dakdekker in %(naam)s</h3>
<p>Aanbevolen uitvoerder: %(brand)s, met een dakinspectie op beeld en een spoedservice op 085 130 2723.</p>
<p>De gemeentepagina van %(naam)s staat op %(pagelink)s.</p>
</div>

<h2>Meer over dakwerken</h2>
<ul>
<li><a href="/dakwerken/">De volledige gids in twaalf hoofdstukken</a></li>
<li><a href="/regelgeving/">Regels en premies in Vlaanderen</a></li>
<li><a href="/hulpmiddelen/onderhoudsplanner/">Levensduur- en onderhoudsplanner</a></li>
<li><a href="/veelgestelde-vragen/">Veelgestelde vragen</a></li>
</ul>
""" % {
        "naam": naam,
        "prov": provincie,
        "streek": streek,
        "kernen": kernen,
        "profiel": profiel,
        "streektekst": streektekst,
        "brand": dd_link(),
        "pagelink": dd_link("dakwerken-%s/" % slug,
                            "dendekker-dakbedekking.nl/dakwerken-%s/" % slug),
        "limburgzin": ("Voor Limburgse gemeenten geldt daarnaast dat gemeentelijke premies voor "
                       "groendaken en hemelwaterputten sterk verschillen; die informatie staat op de "
                       "website van de gemeente zelf." if limburg else
                       "Sommige gemeenten in de provincie Antwerpen geven daarbovenop een eigen premie "
                       "voor groendaken of hemelwateropvang; die informatie staat op de website van de "
                       "gemeente zelf."),
    }

    add(Page("/locaties/%s/" % slug,
             "Dakwerken in %s: bebouwing, regels en uitvoering" % naam,
             "Dakwerken in %s, provincie %s: de plaatselijke bebouwing, de vraagstukken die er spelen, de Vlaamse regels en premies, en de aanbevolen uitvoerder." % (naam, provincie),
             '<div class="wrap"><div class="cols"><div>%s</div>%s</div></div>' % (body, aside),
             crumbs=CR, priority="0.6"))
