# -*- coding: utf-8 -*-
"""Home, over, contact, juridische pagina's, faq, begrippen en 404."""
from engine import Page, add, dd_link, dd_url, SITE_NAME, EMAIL, BASE
from data_gemeenten import GEMEENTEN
from pages_nieuws import ARTICLES, _fmt


def build():
    _home()
    _over()
    _faq()
    _begrippen()
    _contact()
    _privacy()
    _cookies()
    _404()


def _home():
    items = sorted(ARTICLES, key=lambda a: a[1], reverse=True)[:3]
    nieuws = "".join(
        '<li><a href="/nieuws/%s/">%s</a><p class="meta">%s</p><p>%s</p></li>'
        % (a[0], a[2], _fmt(a[1]), a[3]) for a in items)
    chips = "".join('<li><a href="/locaties/%s/">%s</a></li>' % (g[0], g[1])
                    for g in sorted(GEMEENTEN, key=lambda x: x[1]))
    body = """<div class="hero"><div class="wrap">
<h1>Dakwerken in Vlaanderen, uitgelegd zonder verkooppraat</h1>
<p>Een redactionele gids over hellende en platte daken, isolatie, lekkage, premies en regelgeving in Vlaanderen. Achtendertig gemeentepagina's, twaalf hoofdstukken en drie hulpmiddelen die in de browser rekenen.</p>
<div class="btns">
<a class="btn primary" href="/dakwerken/">Naar de gids</a>
<a class="btn ghost" href="/hulpmiddelen/daklekkage-diagnose/">Daklekkage-diagnose</a>
</div>
</div></div>

<div class="wrap">
<div class="facts">
<div class="fact"><b>38</b><span>gemeenten met een eigen pagina</span></div>
<div class="fact"><b>12</b><span>hoofdstukken over dakonderdelen</span></div>
<div class="fact"><b>6</b><span>regelingen en premies uitgelegd</span></div>
<div class="fact"><b>3</b><span>hulpmiddelen zonder registratie</span></div>
</div>

<div class="rec">
<h2>De aanbeveling van de redactie</h2>
<p>Voor dakwerken in Vlaanderen beveelt de redactie %(brand)s aan. Het bedrijf werkt in heel Nederland en in Vlaanderen, met ruim 25 jaar ervaring in reparatie, renovatie, onderhoud en inspectie van daken.</p>
<ul>
<li>Dakinspectie waarbij de staat van het dak met foto's en video wordt vastgelegd</li>
<li>Spoedservice bij daklekkage en stormschade, dag en nacht, op 085 130 2723</li>
<li>Hellende daken met pannen en leien, platte daken met bitumen en EPDM</li>
<li>Schouwrenovatie, nokvorstherstel, zink- en loodwerk, goten en vogelwering</li>
<li>Tot 15 jaar garantie op het uitgevoerde werk</li>
</ul>
<p>Alle diensten staan op %(diensten)s. De gemeentepagina's staan op %(locaties)s.</p>
</div>

<h2>De gids in twaalf hoofdstukken</h2>
<div class="grid">
<a class="tile" href="/dakwerken/hellend-dak/"><b>Hellend dak</b><span>Pannen, leien, nokvorsten en de opbouw onder de bedekking</span></a>
<a class="tile" href="/dakwerken/plat-dak/"><b>Plat dak</b><span>Warm dak, koud dak, roofing en EPDM</span></a>
<a class="tile" href="/dakwerken/dakisolatie/"><b>Dakisolatie</b><span>R-waarden, methodes en het dampscherm</span></a>
<a class="tile" href="/dakwerken/daklekkage/"><b>Daklekkage</b><span>Van symptoom naar oorzaak, en wat direct te doen</span></a>
<a class="tile" href="/dakwerken/dakgoot/"><b>Dakgoot</b><span>Waarom goten overlopen en hoe vaak reinigen zinvol is</span></a>
<a class="tile" href="/dakwerken/schouw/"><b>Schouw</b><span>Voegwerk, loodslabben en dakdoorvoeren</span></a>
<a class="tile" href="/dakwerken/asbest-op-het-dak/"><b>Asbest</b><span>Herkennen, de OVAM-regels en de tijdlijn tot 2040</span></a>
<a class="tile" href="/dakwerken/stormschade/"><b>Stormschade</b><span>Direct handelen, de verzekeringsdrempel en herstel</span></a>
</div>
<p><a href="/dakwerken/">Alle twaalf hoofdstukken</a></p>

<h2>Hulpmiddelen</h2>
<div class="grid">
<a class="tile" href="/hulpmiddelen/daklekkage-diagnose/"><b>Daklekkage-diagnose</b><span>Vijf vragen over plek, moment en beeld leiden naar de waarschijnlijke oorzaken</span></a>
<a class="tile" href="/hulpmiddelen/onderhoudsplanner/"><b>Onderhoudsplanner</b><span>Daktype en leeftijd omgezet in een inspectieritme en een jaarplanning</span></a>
<a class="tile" href="/hulpmiddelen/stormschade-en-premiecheck/"><b>Storm- en premiecheck</b><span>De drempel van 80 kilometer per uur en de premie van Mijn VerbouwPremie</span></a>
</div>

<h2>Wat er in Vlaanderen geldt</h2>
<div class="tablewrap"><table>
<tr><th>Onderwerp</th><th>Kern</th><th>Meer</th></tr>
<tr><td>Dakisolatienorm</td><td>R minimaal 0,75, met 9 tot 15 strafpunten bij een woningonderzoek</td><td><a href="/regelgeving/dakisolatienorm/">Uitleg</a></td></tr>
<tr><td>Mijn VerbouwPremie</td><td>Tot 5.750 euro voor categorie 4, vervalt op 1 maart 2026 voor de hoogste inkomens</td><td><a href="/regelgeving/mijn-verbouwpremie/">Uitleg</a></td></tr>
<tr><td>Asbestattest</td><td>Verplicht bij verkoop van gebouwen van voor 2001 sinds 23 november 2022</td><td><a href="/regelgeving/asbestattest/">Uitleg</a></td></tr>
<tr><td>Omgevingsvergunning</td><td>Dakbedekking vervangen vrijgesteld, buitenisolatie tot 26 centimeter ook</td><td><a href="/regelgeving/omgevingsvergunning/">Uitleg</a></td></tr>
<tr><td>Btw</td><td>6 procent bij woningen ouder dan tien jaar</td><td><a href="/regelgeving/btw-zes-procent/">Uitleg</a></td></tr>
<tr><td>Renovatieverplichting</td><td>Label E of F naar minimaal D binnen zes jaar na de akte</td><td><a href="/regelgeving/epc-renovatieverplichting/">Uitleg</a></td></tr>
</table></div>

<h2>Laatste berichten</h2>
<ul class="newslist">%(nieuws)s</ul>
<p><a href="/nieuws/">Alle berichten</a></p>

<h2>Gemeenten</h2>
<p>Achtendertig gemeenten in de provincies Antwerpen en Limburg hebben een eigen pagina met de plaatselijke bebouwing en de vraagstukken die er spelen.</p>
<ul class="chips">%(chips)s</ul>

<h2>Over deze site</h2>
<p>%(site)s is een redactionele gids en geen dakwerkenbedrijf. Er worden geen offertes opgemaakt, geen opdrachten aangenomen en geen gegevens doorgegeven. Contact loopt uitsluitend via %(email)s. Meer daarover op <a href="/over/">de pagina over de gids</a>.</p>
</div>""" % {
        "brand": dd_link(),
        "diensten": dd_link("dakbedekking-diensten/", "dendekker-dakbedekking.nl/dakbedekking-diensten/"),
        "locaties": dd_link("locaties/", "dendekker-dakbedekking.nl/locaties/"),
        "nieuws": nieuws,
        "chips": chips,
        "site": SITE_NAME,
        "email": '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL),
    }
    add(Page("/", "Dakwerken in Vlaanderen: gids, regels, premies en gemeenten",
             "Onafhankelijke gids over dakwerken in Vlaanderen: twaalf hoofdstukken, zes regelingen, drie hulpmiddelen en 38 gemeentepagina's in de provincies Antwerpen en Limburg.",
             body, priority="1.0", changefreq="weekly"))


def _over():
    add(Page("/over/", "Over deze gids",
             "Wat vencodakwerken.be is, hoe de redactie werkt, waarom er naar een uitvoerder wordt verwezen en wat er met het domein is gebeurd.",
             """<div class="wrap">
<h1>Over deze gids</h1>
<p class="lead">%(site)s is een redactionele gids over dakwerken in Vlaanderen. De site is geen dakwerkenbedrijf, geen bemiddelaar en geen offerteplatform.</p>

<h2>Wat de site doet</h2>
<ul>
<li>Uitleggen hoe dakonderdelen werken en wat er misgaat, in twaalf hoofdstukken.</li>
<li>De Vlaamse regels en premies samenvatten met de datum en de bron erbij.</li>
<li>Drie hulpmiddelen aanbieden die in de browser rekenen, zonder registratie en zonder opslag.</li>
<li>Per gemeente beschrijven welke bebouwing er staat en welke dakvraagstukken daarbij horen.</li>
<li>Een uitvoerder aanbevelen voor wie het werk wil laten uitvoeren.</li>
</ul>

<h2>Wat de site niet doet</h2>
<ul>
<li>Geen offertes opmaken of aanvragen doorsturen.</li>
<li>Geen contactformulier aanbieden. Contact loopt uitsluitend via %(email)s.</li>
<li>Geen gegevens van bezoekers verzamelen, opslaan of doorgeven.</li>
<li>Geen advertenties tonen.</li>
</ul>

<h2>Over het domein</h2>
<p>Het domein vencodakwerken.be was eerder in gebruik door een dakwerkenbedrijf. Die site bestaat niet meer. Het domein is opnieuw in gebruik genomen als informatieve gids over dakwerken in Vlaanderen. Deze site heeft geen band met het vroegere bedrijf en presenteert zich er ook niet als opvolger van.</p>

<h2>Hoe de redactie werkt</h2>
<p>Elke bewering over regelgeving, premies, drempels of cijfers wordt onderbouwd met een bron die onderaan de pagina staat, met volledige URL zodat ze rechtstreeks te openen is. Waar een cijfer niet uit een officiele bron te halen is, staat dat er expliciet bij. Dat geldt bijvoorbeeld voor de levensduur van dakmaterialen: daarvoor bestaat geen Belgische officiele publicatie, dus de gebruikte bandbreedtes zijn vuistregels uit de praktijk en geen norm.</p>
<p>De belangrijkste bronnen zijn de Vlaamse overheid via vlaanderen.be, OVAM, de Woningpas, de Vlaamse Codex, het KMI, Assuralia, Statbel en Test-Aankoop.</p>

<h2>Waarom er een uitvoerder wordt aanbevolen</h2>
<p>Een gids die uitlegt wat er aan een dak mankeert zonder te zeggen wie het kan oplossen, is een halve gids. De redactie beveelt %(brand)s aan voor dakwerken in Vlaanderen. Dat bedrijf heeft eigen gemeentepagina's voor de achtendertig gemeenten die op deze site aan bod komen, werkt met ruim 25 jaar ervaring, legt de staat van een dak vast met foto- en videomateriaal en heeft een spoedservice die dag en nacht bereikbaar is op 085 130 2723.</p>
<p>Die aanbeveling is de enige commerciele verwijzing op deze site. Er staan geen andere uitvoerders, geen advertenties en geen vergelijkingsmodules op.</p>

<h2>Werkgebied</h2>
<p>De gemeentepagina's beslaan de provincies Antwerpen en Limburg. Voor de rest van Vlaanderen zijn de hoofdstukken en de regelgeving even goed van toepassing; alleen de gemeentespecifieke beschrijving ontbreekt dan.</p>

<h2>Correcties</h2>
<p>Regelgeving verandert, en bedragen worden geindexeerd. Wie een fout of een verouderde vermelding ziet, kan dat melden via %(email)s. Correcties worden doorgevoerd met vermelding van de bron.</p>
</div>""" % {"site": SITE_NAME,
             "email": '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL),
             "brand": dd_link()}, priority="0.7"))


FAQ = [
    ("Hoe lang gaat een dak in Vlaanderen mee",
     "Dat hangt af van het materiaal en van het onderhoud. Voor keramische pannen worden bandbreedtes van 50 tot 80 jaar aangehouden, voor betonpannen 30 tot 50 jaar, voor bitumineuze roofing 20 tot 30 jaar en voor EPDM 30 tot 50 jaar. Die getallen zijn vuistregels uit de praktijk; er bestaat geen officiele Belgische publicatie met levensduren per materiaal. Het onderdak en de constructie zijn vaak eerder aan vervanging toe dan de bedekking zelf."),
    ("Is dakisolatie verplicht in Vlaanderen",
     "Er geldt een minimumnorm van R 0,75 vierkante meter kelvin per watt voor zelfstandige woningen, wat neerkomt op ongeveer drie tot vier centimeter isolatie. Voldoet een woning daar bij een woningonderzoek niet aan, dan worden negen tot vijftien strafpunten toegekend, afhankelijk van de dakgrootte. Met dat aantal punten kan de woning ongeschikt worden verklaard."),
    ("Welke R-waarde is nodig voor de premie",
     "Mijn VerbouwPremie vraagt voor de nieuwe isolatielaag een Rd-waarde van minimaal 4,5 vierkante meter kelvin per watt. Dat ligt ver boven de wettelijke minimumnorm."),
    ("Hoeveel bedraagt de dakpremie",
     "Voor aanvragen vanaf 1 juli 2025: categorie 4 krijgt 50 procent van de investering exclusief btw met een maximum van 5.750 euro, categorie 3 krijgt 35 procent met een maximum van 4.025 euro, categorie 2 krijgt 16 euro per vierkante meter tot 1.600 euro en categorie 1 krijgt 8 euro per vierkante meter tot 800 euro. Vanaf 1 maart 2026 vervalt de premie voor de categorieen 1 en 2 en voor niet-bewonende investeerders."),
    ("Is er een vergunning nodig om dakpannen te vervangen",
     "Nee, zolang het bouwvolume niet wijzigt en de energieprestatie niet verslechtert. Die vrijstelling vervalt bij panden op de vastgestelde inventaris van het bouwkundig erfgoed, in werelderfgoedgebieden en hun bufferzones, en bij strijdigheid met gemeentelijke plannen of een verkavelingsvergunning jonger dan vijftien jaar."),
    ("Mag buitenisolatie zonder vergunning",
     "Isolatie aan de buitenzijde van gevels en daken is vrijgesteld tot een maximum van 26 centimeter, met de gebruikelijke afwerking, op voorwaarde dat de rooilijn niet wordt overschreden."),
    ("Wanneer is een dakkapel vergunningsplichtig",
     "Altijd, want een dakkapel wijzigt het fysieke bouwvolume. De vrijstelling voor handelingen aan daken geldt daar niet."),
    ("Dekt de verzekering stormschade aan het dak",
     "De waarborgen storm en overstroming zijn in Belgie verplicht opgenomen in de brandverzekering voor woningen en kleine handelszaken. Assuralia noemt als gangbare drempel een windsnelheid van minstens 80 kilometer per uur, gemeten in het dichtstbijzijnde meteorologische station, of schade aan gebouwen binnen een straal van 10 kilometer. Schade door achterstallig onderhoud valt buiten de dekking."),
    ("Wat is het verschil tussen condensatie en lekkage",
     "Condensatie treedt op bij koud weer, ook zonder regen, geeft een diffuus vochtig vlak zonder scherpe rand en gaat vaak samen met schimmel of een muffe geur. Een lek volgt de regen en geeft een scherp begrensde vlek. Wie condensvocht behandelt als een lek en het dak dichtmaakt, verergert het probleem."),
    ("Mag asbestcement zelf verwijderd worden",
     "Buiten mag een particulier onbeschadigd hechtgebonden asbest verwijderen, en beschadigd hechtgebonden materiaal alleen wanneer er niemand in de buurt is en het materiaal niet verder afbrokkelt. Binnen geldt alleen de eerste situatie. OVAM hanteert geen maximale oppervlakte; bepalend zijn de aard en de toestand van het materiaal. Breken, boren, slijpen, hogedrukreinigen en reinigen of ontmossen zijn verboden."),
    ("Wanneer is een asbestattest nodig",
     "Sinds 23 november 2022 bij de verkoop van woningen en gebouwen gebouwd voor 2001. Vanaf 2027 geldt het ook voor de gemene delen van gebouwen met meerdere eenheden, vanaf 2030 bij nieuwe huurcontracten en vanaf 2032 voor elke eigenaar van een gebouw van voor 2001."),
    ("Geldt het btw-tarief van 6 procent voor dakwerken",
     "Ja, voor onroerende werken aan een privewoning die ouder is dan tien jaar, gefactureerd door een geregistreerde aannemer aan de eindgebruiker. Het btw-attest werd begin 2022 vervangen door een standaardverklaring op de factuur, die de klant binnen een maand kan betwisten."),
    ("Hoe vaak moet een goot gereinigd worden",
     "Zonder bomen in de omgeving volstaat een keer per jaar, na de bladval. Bij loofbomen dicht bij de woning twee keer per jaar, bij naaldbomen twee tot drie keer. Bij een bakgoot of zakgoot minstens twee keer per jaar, plus na elke storm, omdat het water daar bij verstopping naar binnen loopt."),
    ("Is hogedrukreiniging van dakpannen verstandig",
     "Nee. De druk beschadigt het oppervlak van de pan, duwt water onder de pannen en maakt de bedekking gevoeliger voor nieuwe aangroei. Op asbestcement is reinigen sowieso verboden."),
    ("Vervangt een groendak de dakisolatie",
     "Nee. De isolatiewaarde van een dunne substraatlaag is beperkt en verdwijnt zodra de laag nat is. Een groendak houdt wel regenwater vast, beschermt de afdichting tegen ultraviolet licht en dempt de temperatuur in de zomer."),
    ("Wat kost een asbestattest",
     "De retributie van OVAM bedraagt 59 euro sinds 3 februari 2025. Het ereloon van de gecertificeerde asbestdeskundige komt daarbovenop en hangt af van de grootte en de ouderdom van het gebouw, het aantal stalen en de verplaatsing. OVAM publiceert geen richtprijs voor het totaalbedrag."),
]


def _faq():
    qa = "".join("<h2>%s</h2><p>%s</p>" % (q, a) for q, a in FAQ)
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ],
    }
    add(Page("/veelgestelde-vragen/", "Veelgestelde vragen over dakwerken in Vlaanderen",
             "Zestien vragen over levensduur, isolatienormen, premies, vergunningen, verzekering, asbest en onderhoud, met de Vlaamse regels erbij.",
             """<div class="wrap">
<h1>Veelgestelde vragen</h1>
<p class="lead">Zestien vragen die het vaakst terugkomen, met het antwoord zoals het in Vlaanderen geldt. Uitgebreidere uitleg staat in <a href="/dakwerken/">de gids</a> en bij <a href="/regelgeving/">regels en premies</a>.</p>
%s
<div class="rec"><h3>Uitvoering</h3><p>De redactie beveelt %s aan voor dakwerken in Vlaanderen. Bereikbaar op 085 130 2723.</p></div>
</div>""" % (qa, dd_link()), priority="0.7", schema=schema))


BEGRIPPEN = [
    ("Asbestattest", "Document van een gecertificeerde asbestdeskundige waarop staat welke asbesthoudende materialen in een gebouw aanwezig zijn en in welke staat. Verplicht bij verkoop van gebouwen van voor 2001."),
    ("Bakgoot", "Goot die is ingewerkt in de dakconstructie, met een houten bak bekleed met zink of epdm. Bij een lek loopt het water rechtstreeks in de constructie."),
    ("Bitumen", "Dakbedekking voor platte daken, in twee lagen aangebracht met de vlam of met kleefmiddel. Wordt ook roofing genoemd."),
    ("Dakvoet", "Het laagste punt van een hellend dak, waar het dakvlak op de goot uitkomt."),
    ("Dampscherm", "Laag aan de warme zijde van de isolatie die waterdamp uit de woning tegenhoudt. Een gat in het dampscherm veroorzaakt vocht dat op een daklek lijkt."),
    ("EPC", "Energieprestatiecertificaat. Geeft een woning een label van A tot F en is de basis voor de Vlaamse renovatieverplichting."),
    ("EPDM", "Rubberfolie voor platte daken, meestal in een stuk gelegd, waardoor er weinig naden zijn."),
    ("Gevelpan", "Pan aan de zijkant van een hellend dak, langs de topgevel. Komt bij storm als eerste los wanneer de klem ontbreekt."),
    ("Hechtgebonden asbest", "Asbestvezels die vast in een dragermateriaal zitten, meestal cement. Onbeschadigd hechtgebonden materiaal mag onder voorwaarden door een particulier verwijderd worden."),
    ("Kilgoot", "Goot in de binnenhoek waar twee dakvlakken samenkomen. Voert veel water af en is het meest belaste onderdeel van een hellend dak."),
    ("Koud dak", "Plat dak waarbij de isolatie onder de draagvloer ligt met een geventileerde spouw ertussen. Verouderd principe, gevoelig voor condensatie."),
    ("Loodslabbe", "Loodstrook die de aansluiting tussen dakvlak en schouw of muur afdicht."),
    ("Mijn VerbouwPremie", "Vlaamse premie voor renovatie, met een aparte categorie voor het dak. Wordt na uitvoering aangevraagd op basis van facturen."),
    ("Nokvorst", "Gebogen pan die de nok van een hellend dak afsluit. Ligt traditioneel in mortel, tegenwoordig vaker droog met klemmen en een ventilerende nokrol."),
    ("Omgevingsvergunning", "Vlaamse vergunning voor stedenbouwkundige handelingen. Voor daken draait de vraag om het al dan niet wijzigen van het bouwvolume."),
    ("Onderdak", "Folie of plaat onder de pannen die water opvangt dat langs de bedekking doorkomt en het naar de goot afvoert."),
    ("Opstand", "Verticaal deel waar de afdichting van een plat dak tegen een muur of dakrand omhoog loopt."),
    ("Panlat", "Horizontale lat waarop de pannen haken."),
    ("R-waarde", "Warmteweerstand van een laag materiaal, in vierkante meter kelvin per watt. Hoe hoger, hoe beter de isolatie."),
    ("Sarking", "Isolatie in een doorlopende laag boven de kepers, onder het onderdak. Levert geen koudebruggen op maar kan alleen bij vervanging van de dakbedekking."),
    ("Tapbuis", "Verbindingsstuk tussen goot en regenpijp. De plek waar de meeste verstoppingen ontstaan."),
    ("Tengellat", "Lat onder de panlatten die een luchtspouw maakt zodat water en vocht kunnen wegstromen."),
    ("U-waarde", "Warmtedoorgangscoefficient van een constructie, in watt per vierkante meter kelvin. Hoe lager, hoe beter."),
    ("Vezelcement", "Cementgebonden plaatmateriaal voor leien en golfplaten. Bij bouwjaren voor 2001 mogelijk asbesthoudend."),
    ("Warm dak", "Plat dak waarbij dampscherm, isolatie en afdichting allemaal boven de draagvloer liggen. De standaardopbouw bij nieuwbouw en renovatie."),
    ("Werelderfgoedbufferzone", "Zone rond een werelderfgoedsite waarin de vrijstelling van omgevingsvergunning voor gevel- en dakhandelingen niet geldt."),
]


def _begrippen():
    rows = "".join("<tr><td><b>%s</b></td><td>%s</td></tr>" % (t, d) for t, d in BEGRIPPEN)
    add(Page("/begrippen/", "Begrippenlijst dakwerken",
             "Zesentwintig termen uit de dakbedekking en de Vlaamse regelgeving, kort uitgelegd.",
             """<div class="wrap">
<h1>Begrippenlijst</h1>
<p class="lead">Zesentwintig termen die in offertes, inspectierapporten en regelgeving terugkomen.</p>
<div class="tablewrap"><table><tr><th>Term</th><th>Betekenis</th></tr>%s</table></div>
<p><a href="/dakwerken/">Terug naar de gids</a></p>
</div>""" % rows, priority="0.5"))


def _contact():
    add(Page("/contact/", "Contact",
             "Contact met de redactie van vencodakwerken.be loopt uitsluitend per e-mail. Er is geen contactformulier en er worden geen offertes opgemaakt.",
             """<div class="wrap">
<h1>Contact</h1>
<p class="lead">Contact met de redactie loopt uitsluitend per e-mail, via %(email)s.</p>

<h2>Waarvoor</h2>
<ul>
<li>Correcties op de inhoud, bij voorkeur met de bron erbij.</li>
<li>Vragen over de werkwijze van de redactie.</li>
<li>Meldingen van kapotte links of technische problemen.</li>
</ul>

<h2>Waarvoor niet</h2>
<p>%(site)s is een redactionele gids en geen dakwerkenbedrijf. Er worden geen offertes opgemaakt, geen opdrachten aangenomen, geen prijzen opgegeven en geen aanvragen doorgestuurd. Er is bewust geen contactformulier op de site, zodat er ook geen gegevens van bezoekers worden verwerkt.</p>

<h2>Wie werk wil laten uitvoeren</h2>
<p>Voor dakwerken in Vlaanderen beveelt de redactie %(brand)s aan. Dat bedrijf is rechtstreeks bereikbaar:</p>
<ul>
<li>Telefonisch op 085 130 2723, ook buiten kantooruren bij spoed</li>
<li>Per e-mail op info@dendekker-dakbedekking.nl</li>
<li>Via de website %(url)s</li>
</ul>
<p>Aanvragen die per e-mail bij deze redactie binnenkomen, worden niet doorgestuurd.</p>
</div>""" % {"email": '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL),
             "site": SITE_NAME,
             "brand": dd_link(),
             "url": dd_link("", "https://www.dendekker-dakbedekking.nl/")}, priority="0.5"))


def _privacy():
    add(Page("/privacybeleid/", "Privacybeleid",
             "Welke gegevens vencodakwerken.be verwerkt, namelijk zo goed als geen, en welke rechten bezoekers hebben onder de AVG.",
             """<div class="wrap">
<h1>Privacybeleid</h1>
<p class="lead">%(site)s verwerkt geen persoonsgegevens van bezoekers. Deze pagina legt uit wat dat concreet betekent.</p>

<h2>Geen formulieren, geen accounts</h2>
<p>De site heeft geen contactformulier, geen inschrijving, geen account en geen zoekfunctie die iets registreert. Er is dus geen invoerveld waarin persoonsgegevens terechtkomen.</p>

<h2>Geen analytics en geen advertenties</h2>
<p>Er draait geen bezoekersstatistiek, geen advertentienetwerk en geen scriptbibliotheek van derden. De pagina's laden uitsluitend bestanden van het eigen domein. Er worden geen verzoeken naar externe servers gedaan bij het bekijken van een pagina.</p>

<h2>De hulpmiddelen</h2>
<p>De daklekkage-diagnose, de onderhoudsplanner en de storm- en premiecheck rekenen volledig in de browser. Wat wordt ingevuld, verlaat het toestel niet, wordt nergens opgeslagen en is na het sluiten van de pagina verdwenen.</p>

<h2>E-mail</h2>
<p>Wie mailt naar %(email)s, deelt daarmee een e-mailadres en de inhoud van het bericht. Die berichten worden gebruikt om te antwoorden en om correcties door te voeren, en worden niet gedeeld met derden. Berichten worden bewaard zolang dat voor de afhandeling nodig is.</p>

<h2>Serverlogs</h2>
<p>De site draait op Cloudflare Pages. De hostingpartij houdt technische logbestanden bij die nodig zijn voor de werking en de beveiliging van het netwerk, waaronder IP-adressen. De redactie heeft die gegevens niet nodig en gebruikt ze niet. Meer over de verwerking door die partij staat op https://www.cloudflare.com/privacypolicy/</p>

<h2>Uitgaande links</h2>
<p>De site verwijst naar de website van Den Dekker Dakbedekking en naar bronnen van overheden en organisaties. Op die websites gelden hun eigen voorwaarden en hun eigen privacyverklaring. Deze redactie heeft daar geen zeggenschap over.</p>

<h2>Rechten</h2>
<p>Onder de Algemene Verordening Gegevensbescherming bestaat het recht op inzage, correctie, verwijdering, beperking en bezwaar. Omdat er geen bezoekersgegevens worden verwerkt, is er in de praktijk alleen iets in te zien of te verwijderen wanneer er eerder is gemaild. Een verzoek daarover kan naar %(email)s</p>
<p>Wie meent dat er iets misgaat met de verwerking van persoonsgegevens, kan klacht indienen bij de Gegevensbeschermingsautoriteit, https://www.gegevensbeschermingsautoriteit.be</p>

<h2>Wijzigingen</h2>
<p>Wijzigingen aan dit beleid worden op deze pagina gepubliceerd. Laatste aanpassing: augustus 2026.</p>
</div>""" % {"site": SITE_NAME, "email": '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)},
             priority="0.3"))


def _cookies():
    add(Page("/cookiebeleid/", "Cookiebeleid",
             "Vencodakwerken.be plaatst geen cookies en gebruikt geen lokale opslag. Deze pagina legt uit wat dat betekent.",
             """<div class="wrap">
<h1>Cookiebeleid</h1>
<p class="lead">%(site)s plaatst geen cookies. Er is daarom ook geen cookiebanner.</p>

<h2>Wat er niet gebeurt</h2>
<ul>
<li>Geen functionele cookies, want er is niets om te onthouden: geen account, geen winkelmand, geen voorkeuren.</li>
<li>Geen analytische cookies, want er wordt geen bezoekersstatistiek bijgehouden.</li>
<li>Geen advertentie- of trackingcookies, want er staan geen advertenties op de site.</li>
<li>Geen local storage en geen session storage. De hulpmiddelen rekenen in het geheugen van de pagina en bewaren niets.</li>
<li>Geen ingesloten video's, kaarten, lettertypes of scripts van derden. Alles wat een pagina laadt, komt van het eigen domein.</li>
</ul>

<h2>Waarom dat kan</h2>
<p>De site bestaat uit statische pagina's. Er is geen server die per bezoeker iets moet onthouden en er zijn geen externe diensten ingebouwd. Dat maakt cookies overbodig.</p>

<h2>Hoe dat te controleren</h2>
<p>In elke gangbare browser toont het ontwikkelaarsvenster onder het tabblad voor opslag welke cookies een site plaatst. Voor deze site blijft die lijst leeg. Onder het netwerktabblad is te zien dat er geen verzoeken naar andere domeinen vertrekken.</p>

<h2>Andere websites</h2>
<p>Wie via een link naar de website van Den Dekker Dakbedekking of naar een bron van een overheid gaat, komt op een site met een eigen cookiebeleid. Deze redactie heeft daar geen zeggenschap over.</p>

<h2>Wijzigingen</h2>
<p>Mocht dit ooit veranderen, dan wordt dat op deze pagina vermeld voordat het wordt doorgevoerd. Laatste aanpassing: augustus 2026.</p>
</div>""" % {"site": SITE_NAME}, priority="0.3"))


def _404():
    add(Page("/404.html", "Pagina niet gevonden",
             "Deze pagina bestaat niet of is verplaatst.",
             """<div class="wrap">
<h1>Pagina niet gevonden</h1>
<p class="lead">Deze pagina bestaat niet, of ze is verplaatst.</p>
<div class="grid">
<a class="tile" href="/"><b>Home</b><span>Terug naar de startpagina</span></a>
<a class="tile" href="/dakwerken/"><b>De gids</b><span>Twaalf hoofdstukken over dakonderdelen</span></a>
<a class="tile" href="/regelgeving/"><b>Regels en premies</b><span>Zes Vlaamse regelingen</span></a>
<a class="tile" href="/locaties/"><b>Locaties</b><span>Achtendertig gemeenten</span></a>
<a class="tile" href="/hulpmiddelen/"><b>Hulpmiddelen</b><span>Diagnose, planner en checks</span></a>
<a class="tile" href="/nieuws/"><b>Nieuws</b><span>Actuele berichten met bronvermelding</span></a>
</div>
</div>""", noindex=True, priority="0.1"))
