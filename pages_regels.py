# -*- coding: utf-8 -*-
"""Regels en premies in Vlaanderen."""
from engine import Page, add, dd_link

CR = [("/regelgeving/", "Regels en premies")]

ITEMS = [
    ("mijn-verbouwpremie", "Mijn VerbouwPremie voor het dak",
     "Bedragen per categorie, de Rd-eis van 4,5 en wat er op 1 maart 2026 verandert"),
    ("dakisolatienorm", "De Vlaamse dakisolatienorm",
     "R 0,75 als wettelijk minimum en het strafpuntensysteem"),
    ("asbestattest", "Asbestattest",
     "Verplicht bij verkoop sinds 23 november 2022, geldigheid en tijdlijn"),
    ("omgevingsvergunning", "Omgevingsvergunning voor dakwerken",
     "Wat vrijgesteld is en wanneer de vrijstelling vervalt"),
    ("btw-zes-procent", "Btw van 6 procent",
     "De leeftijdsgrens van tien jaar en de verklaring op de factuur"),
    ("epc-renovatieverplichting", "EPC en de renovatieverplichting",
     "Label E of F naar minimaal D, termijn van zes jaar"),
]


def sources(items):
    return '<h2>Bronnen</h2><ul class="src">%s</ul>' % "".join("<li>%s</li>" % i for i in items)


def _p(slug, title, desc, body):
    aside = ('<aside><div class="card"><h3>Meer over regels en premies</h3>'
             '<ul style="margin:0;padding-left:18px">%s</ul></div></aside>'
             % "".join('<li><a href="/regelgeving/%s/">%s</a></li>' % (s, t)
                       for s, t, _ in ITEMS if s != slug))
    add(Page("/regelgeving/%s/" % slug, title, desc,
             '<div class="wrap"><div class="cols"><div>%s</div>%s</div></div>' % (body, aside),
             crumbs=CR, priority="0.7"))


def build():
    tiles = "".join('<a class="tile" href="/regelgeving/%s/"><b>%s</b><span>%s</span></a>'
                    % (s, t, d) for s, t, d in ITEMS)
    add(Page("/regelgeving/",
             "Regels en premies voor dakwerken in Vlaanderen",
             "Mijn VerbouwPremie, de dakisolatienorm, het asbestattest, de omgevingsvergunning, het btw-tarief van 6 procent en de renovatieverplichting, met de stand van augustus 2026.",
             """<div class="wrap">
<h1>Regels en premies</h1>
<p class="lead">Wie in Vlaanderen dakwerken laat uitvoeren, krijgt met zes regelingen te maken. Deze pagina's zetten per regeling op een rij wat geldt, met de datum en de bron erbij. De stand is die van augustus 2026.</p>
<div class="grid">%s</div>
<div class="note">Regelgeving verandert. Voor Mijn VerbouwPremie geldt bijvoorbeeld dat de premie voor de hoogste inkomenscategorieen op 1 maart 2026 wegvalt. De officiele bron blijft leidend, en die staat telkens onderaan de pagina vermeld met volledige URL.</div>
<h2>Volgorde die tijd bespaart</h2>
<ol>
<li>Nagaan of het pand op de vastgestelde inventaris van het bouwkundig erfgoed staat of in een werelderfgoedbufferzone ligt. Dat bepaalt of vrijstellingen gelden.</li>
<li>Nagaan of er nog asbesthoudend materiaal op het dak ligt. Dat bepaalt de werkwijze en levert een asbestbonus op.</li>
<li>De premiecategorie opzoeken op basis van het inkomen. Dat bepaalt of de premie een percentage of een bedrag per vierkante meter is.</li>
<li>Pas daarna offertes vergelijken, want de premievoorwaarden stellen eisen aan de Rd-waarde van de isolatie en aan de facturatie.</li>
</ol>
</div>""" % tiles, priority="0.8"))

    _p("mijn-verbouwpremie", "Mijn VerbouwPremie voor het dak: bedragen en voorwaarden",
       "Premiebedragen per inkomenscategorie voor dakwerken, de eis van Rd 4,5, de asbestbonus en de wijziging vanaf 1 maart 2026.",
       """<h1>Mijn VerbouwPremie voor het dak</h1>
<p class="lead">Mijn VerbouwPremie is de Vlaamse premie voor renovatie. Voor de categorie dak gelden bedragen die afhangen van het inkomen van de aanvrager. De premie wordt aangevraagd na uitvoering, op basis van facturen.</p>

<h2>Bedragen voor aanvragen vanaf 1 juli 2025</h2>
<div class="tablewrap"><table>
<tr><th>Categorie</th><th>Premie</th><th>Maximum</th></tr>
<tr><td>Categorie 4, laagste inkomens, en verhuurders aan een woonmaatschappij</td><td>50 procent van de investering exclusief btw</td><td>5.750 euro</td></tr>
<tr><td>Categorie 3</td><td>35 procent exclusief btw</td><td>4.025 euro</td></tr>
<tr><td>Categorie 2</td><td>16 euro per vierkante meter</td><td>1.600 euro</td></tr>
<tr><td>Categorie 1 en niet-bewonende investeerders</td><td>8 euro per vierkante meter</td><td>800 euro</td></tr>
<tr><td>Asbestbonus bij gelijktijdige verwijdering</td><td>8 euro per vierkante meter extra</td><td>bovenop het bovenstaande</td></tr>
</table></div>
<p>Het aanvaardbare factuurbedrag ligt tussen 1.000 en 11.500 euro exclusief btw. Alleen de categorieen 1 en 2 werken met een bedrag per vierkante meter; voor de categorieen 3 en 4 is de premie een percentage van de factuur.</p>

<h2>Voorwaarden</h2>
<ul>
<li>De nieuwe isolatie heeft een Rd-waarde van minimaal 4,5 vierkante meter kelvin per watt.</li>
<li>De werken zijn uitgevoerd door een aannemer, met factuur. Doe-het-zelfwerk komt voor deze premie niet in aanmerking.</li>
<li>Facturen zijn op de aanvraagdatum maximaal twee jaar oud.</li>
</ul>

<h2>Wat onder de categorie dak valt</h2>
<p>Bij een hellend dak: dakisolatie, onderdak, dakstructuur, de waterdichte bedekking, behandeling van de houten structuur, dakdoorbrekingen zoals dakramen en lichtkoepels met een Ug van maximaal 1,0 watt per vierkante meter kelvin, dakkapellen, dakgoten en afvoerpijpen. Bij een plat dak: dakisolatie, de waterdichte bedekking, dakgoten en afvoerpijpen.</p>
<p>Dat is ruimer dan alleen het isolatiemateriaal. Wie het dakvlak vernieuwt en tegelijk isoleert, brengt het volledige pakket in.</p>

<h2>Wijziging op 1 maart 2026</h2>
<p>Vanaf 1 maart 2026 verdwijnt de premie voor de categorieen 1 en 2 en voor niet-bewonende investeerders. Die groepen kunnen daarna alleen nog een premie aanvragen voor een warmtepomp of warmtepompboiler, tot en met 31 december 2027. Voor de categorieen 3 en 4 verandert er niets. Vanaf dezelfde datum komen niet-woongebouwen niet meer in aanmerking.</p>
<p>Bouwunie meldt dat de premie daarmee wegvalt voor de 30 procent hoogste inkomens, met als grens 42.340 euro bruto voor alleenstaanden en 59.270 euro bruto voor koppels, verhoogd met 4.320 euro per persoon ten laste. De geindexeerde grensbedragen per categorie staan op de site van de Vlaamse overheid.</p>
%s
%s""" % ('<div class="rec"><h3>Uitvoering</h3><p>De premie vraagt een aannemersfactuur en een isolatie met Rd van minstens 4,5. Beide punten horen in de offerte te staan voordat het werk begint.</p><p>De redactie beveelt %s aan voor dakwerken in Vlaanderen.</p></div>' % dd_link("dakrenovatie/", "dendekker-dakbedekking.nl/dakrenovatie/"),
       sources([
           "Mijn VerbouwPremie voor dak: https://www.vlaanderen.be/premies-voor-renovatie/mijn-verbouwpremie/mijn-verbouwpremie-voor-dak",
           "Wijzigingen Mijn VerbouwPremie vanaf 2026: https://www.vlaanderen.be/premies-voor-renovatie/mijn-verbouwpremie/wijzigingen-mijn-verbouwpremie-vanaf-2026",
           "Bouwunie over de inkomensgrenzen vanaf 2026: https://www.bouwunie.be/nl/nieuws/renovatiesteun-wijzigt-vanaf-2026",
       ])))

    _p("dakisolatienorm", "De Vlaamse dakisolatienorm en het strafpuntensysteem",
       "R van 0,75 als wettelijk minimum voor zelfstandige woningen, de strafpunten sinds 2020 en het verschil met de premievoorwaarde.",
       """<h1>De dakisolatienorm</h1>
<p class="lead">Vlaanderen legt een minimumnorm op voor dakisolatie in zelfstandige woningen. Die norm is een warmteweerstand van 0,75 vierkante meter kelvin per watt, wat neerkomt op ongeveer drie tot vier centimeter isolatiemateriaal.</p>

<h2>Wat de norm inhoudt</h2>
<p>De norm geldt sinds 2015 voor alle zelfstandige woningen. Voldoet een woning er bij een woningonderzoek niet aan, dan worden sinds 1 januari 2020 negen tot vijftien strafpunten toegekend, afhankelijk van de grootte van het dak. Met dat aantal punten kan de woning ongeschikt worden verklaard door de burgemeester.</p>
<p>In het technisch verslag geldt een oppervlaktedifferentiatie: een gebrek van categorie I bij een dakoppervlakte tot en met 16 vierkante meter, categorie II bij meer dan 16 vierkante meter. Daken kleiner dan 2 vierkante meter blijven buiten beschouwing. De rubriek heet 251 in het ministerieel besluit van 26 november 2020.</p>

<h2>Uitzondering</h2>
<p>De sancties bij ongeschiktverklaring gelden niet wanneer de eigenaar de woning volledig en uitsluitend als hoofdverblijfplaats gebruikt en niet over een andere woning beschikt.</p>

<h2>Waarom de norm laag ligt</h2>
<p>Een R-waarde van 0,75 is een ondergrens uit de woningkwaliteitsregelgeving, geen energienorm. Ter vergelijking: Mijn VerbouwPremie eist Rd 4,5 voor de nieuwe isolatielaag, en de energiedoelstelling 2050 gaat uit van een U-waarde van maximaal 0,24 watt per vierkante meter kelvin voor daken. Dat komt neer op ongeveer 12 centimeter PUR of 14 centimeter minerale wol.</p>
<div class="note">Een woning kan dus aan de wettelijke norm voldoen en tegelijk zwaar onder de premie- en energiedoelstellingen zitten. Wie isoleert, kijkt beter naar de premievoorwaarde dan naar de norm.</div>

<h2>Voor verhuurders</h2>
<p>Bij huurwoningen wordt de norm getoetst bij een conformiteitsonderzoek. Een woning zonder dakisolatie of zonder aantoonbare dakisolatie krijgt de strafpunten van rubriek 251. Dat maakt de norm in de huurmarkt een concreet risico, niet alleen een aanbeveling.</p>
%s""" % sources([
           "Vlaanderen over de dakisolatienorm en de strafpunten: https://www.vlaanderen.be/bouwen-wonen-en-energie/energie-besparen/dakisolatie-verplicht-voor-woningen-en-huurwoningen",
           "Woningpas, minimale vereisten en oppervlaktedifferentiatie: https://woningpas.vlaanderen.be/web/woningkwaliteit/energiezuinige-woning/minimale-vereisten",
           "Vlaamse Codex, rubriek 251 in het ministerieel besluit van 26 november 2020: https://codex.vlaanderen.be/PrintDocument.ashx?id=1033955&geannoteerd=true",
           "Woningpas, energiedoelstellingen 2050: https://woningpas.vlaanderen.be/web/woningkwaliteit/energiezuinige-woning/minimale-vereisten/energiedoelstellingen-2050",
       ]))

    _p("asbestattest", "Asbestattest: verplichting, geldigheid en tijdlijn",
       "Sinds 23 november 2022 verplicht bij verkoop van gebouwen van voor 2001, met de retributie, de geldigheidsduur en de mijlpalen tot 2040.",
       """<h1>Asbestattest</h1>
<p class="lead">Het asbestattest beschrijft welke asbesthoudende materialen in een gebouw aanwezig zijn en in welke staat. Het wordt opgemaakt door een gecertificeerde asbestdeskundige na een inspectie ter plaatse.</p>

<h2>Wanneer verplicht</h2>
<p>Sinds 23 november 2022 is een asbestattest verplicht bij de verkoop van woningen en gebouwen die gebouwd zijn voor 2001. De verkoper laat het opmaken en bezorgt het aan de koper.</p>

<h2>Geldigheid en kostprijs</h2>
<ul>
<li>Tien jaar in standaardgevallen.</li>
<li>Vijf jaar wanneer er risicovolle asbestmaterialen aanwezig zijn.</li>
<li>Onbeperkt sinds 8 april 2024 voor attesten waarop geen enkel asbesthoudend materiaal staat.</li>
</ul>
<p>De retributie van OVAM bedraagt 59 euro, verhoogd van 50 euro op 3 februari 2025 volgens de tweejaarlijkse indexering in Vlarema. Daarbovenop komt het ereloon van de deskundige, dat varieert met de grootte en de ouderdom van het gebouw, het aantal stalen en de verplaatsing. OVAM publiceert geen richtprijs voor dat totaalbedrag.</p>

<h2>Tijdlijn</h2>
<div class="tablewrap"><table>
<tr><th>Jaar</th><th>Mijlpaal</th></tr>
<tr><td>2027</td><td>Attest verplicht voor de gemene delen van gebouwen met meerdere eenheden</td></tr>
<tr><td>2030</td><td>Verhuurders bezorgen een attest bij nieuwe huurcontracten</td></tr>
<tr><td>2032</td><td>Elke eigenaar van een gebouw van voor 2001 beschikt over een geldig attest</td></tr>
<tr><td>2034</td><td>De meest risicovolle toepassingen zijn weggenomen</td></tr>
<tr><td>2040</td><td>Alle overige toepassingen in slechte staat zijn verwijderd</td></tr>
</table></div>

<h2>Wat het attest betekent voor het dak</h2>
<p>Op een attest komen dakleien, golfplaten, dakgoten, schouwkanalen en hemelwaterafvoeren in vezelcement terug wanneer het gebouw van voor 2001 dateert. Het attest legt geen verwijderplicht op voor materiaal in goede staat, maar het maakt de aanwezigheid ervan wel officieel bekend bij verkoop, wat de prijsvorming beinvloedt.</p>
<p>Wie het dak toch vernieuwt, combineert de verwijdering met de werken. Dat levert binnen Mijn VerbouwPremie een asbestbonus op van 8 euro per vierkante meter. De praktische regels over zelf verwijderen staan in het hoofdstuk <a href="/dakwerken/asbest-op-het-dak/">asbest op het dak</a>.</p>
%s""" % sources([
           "OVAM over het asbestattest: https://ovam.vlaanderen.be/asbestattest",
           "OVAM, veelgestelde vragen: https://ovam.vlaanderen.be/veelgestelde-vragen-over-het-asbestattest",
           "OVAM over de verhoging van de retributie: https://ovam.vlaanderen.be/w/update-niewsbericht-verhoging-retributie",
           "OVAM, actieplan asbestafbouw: https://ovam.vlaanderen.be/actieplan-asbestafbouw",
       ]))

    _p("omgevingsvergunning", "Omgevingsvergunning voor dakwerken in Vlaanderen",
       "Welke dakhandelingen vrijgesteld zijn van omgevingsvergunning, de grens van 26 centimeter buitenisolatie en de gevallen waarin de vrijstelling vervalt.",
       """<h1>Omgevingsvergunning voor dakwerken</h1>
<p class="lead">Het Vlaamse vrijstellingenbesluit somt de handelingen op waarvoor geen omgevingsvergunning nodig is. Voor daken draait alles om een enkel criterium: verandert het fysieke bouwvolume, of niet.</p>

<h2>Vrijgesteld</h2>
<ul>
<li><strong>Artikel 2.1, 2 graad.</strong> Handelingen aan gevels en daken, zonder de energieprestatie van het gebouw te verslechteren en zonder het fysieke bouwvolume te wijzigen. Het vervangen van dakbedekking valt hieronder.</li>
<li><strong>Artikel 2.1, 2/1 graad.</strong> Het aanbrengen van isolatie, met de gebruikelijke afwerking, aan de buitenzijde van gevels en daken tot maximaal 26 centimeter, op voorwaarde dat de rooilijn niet wordt overschreden.</li>
</ul>

<h2>Vergunningsplichtig</h2>
<p>Elke wijziging van het fysieke bouwvolume of van de dakvorm. Een dakkapel wijzigt het volume en is dus niet vrijgesteld. Een dakraam wordt in artikel 2.1 niet als aparte handeling genoemd; een dakraam dat het volume niet wijzigt valt in de praktijk onder handelingen aan daken, maar dat staat niet met zoveel woorden in de tekst. Navraag bij de gemeente geeft daar uitsluitsel over.</p>

<h2>Wanneer de vrijstelling vervalt</h2>
<div class="tablewrap"><table>
<tr><th>Situatie</th><th>Grondslag</th></tr>
<tr><td>Werelderfgoedgebieden en hun bufferzones</td><td>Artikel 2.2</td></tr>
<tr><td>Gebouwen op de vastgestelde inventaris van het bouwkundig erfgoed</td><td>Artikel 2.2</td></tr>
<tr><td>Strijd met een gemeentelijk ruimtelijk uitvoeringsplan, een bijzonder plan van aanleg of een verkavelingsvergunning jonger dan vijftien jaar</td><td>Artikel 1.4</td></tr>
<tr><td>Verplichte milieueffectrapportage, passende beoordeling of mobiliteitsstudie</td><td>Artikel 1.5</td></tr>
</table></div>
<p>Voor beschermde monumenten en beschermde stads- of dorpsgezichten geldt bovendien afzonderlijke erfgoedregelgeving, met een toelating van het agentschap Onroerend Erfgoed. Dat staat los van het vrijstellingenbesluit.</p>
<div class="note">In de Kempen raakt dit onder meer de Koloniegebieden van Wortel en Merksplas, die sinds 2021 op de Werelderfgoedlijst van UNESCO staan, en de beschermde stadskernen van onder meer Bree en Maaseik.</div>

<h2>Melding of vergunning</h2>
<p>Werken die niet vrijgesteld zijn, verlopen via het Omgevingsloket. De gemeente is het aanspreekpunt. Wie start zonder vergunning waar die wel nodig was, riskeert een stakingsbevel en een herstelvordering, ook wanneer het werk al is uitgevoerd.</p>
%s""" % sources([
           "Besluit van de Vlaamse Regering tot bepaling van stedenbouwkundige handelingen waarvoor geen omgevingsvergunning nodig is: https://codex.vlaanderen.be/portals/codex/documenten/1019375.html",
       ]))

    _p("btw-zes-procent", "Btw van 6 procent bij dakwerken",
       "De voorwaarde dat de woning ouder is dan tien jaar, de verklaring op de factuur sinds 2022 en de wijzigingen van 2025.",
       """<h1>Btw van 6 procent</h1>
<p class="lead">Onroerende werken aan een privewoning die ouder is dan tien jaar vallen onder het verlaagde btw-tarief van 6 procent. Dakwerken horen bij die categorie.</p>

<h2>Voorwaarden</h2>
<ul>
<li>De woning is ouder dan tien jaar, gerekend vanaf de eerste ingebruikname.</li>
<li>De woning wordt hoofdzakelijk privaat gebruikt.</li>
<li>De werken worden gefactureerd door een geregistreerde aannemer, rechtstreeks aan de eindgebruiker.</li>
</ul>

<h2>De verklaring op de factuur</h2>
<p>Het verplichte btw-attest is begin 2022 afgeschaft en vervangen door een standaardverklaring op de factuur zelf. De klant heeft een maand na ontvangst van de factuur om die verklaring schriftelijk te betwisten. Gebeurt dat niet, dan draagt de klant de verantwoordelijkheid voor de correcte toepassing van het tarief.</p>
<p>Dat betekent in de praktijk dat de factuur bij ontvangst wordt nagekeken op de vermelde bouwjaargegevens, niet pas bij een latere controle.</p>

<h2>Wijzigingen in 2025 en 2026</h2>
<p>De programmawet die op 29 juli 2025 in het Belgisch Staatsblad verscheen, wijzigt het btw-regime voor verwarmingsinstallaties op fossiele brandstoffen en voor afbraak en heropbouw. Er gelden overgangsmaatregelen voor contracten die uiterlijk op 28 juli 2025 zijn gesloten, met facturatie tot 30 juni 2026. De regeling van 6 procent voor afbraak en heropbouw werd permanent vanaf 1 juli 2025. De circulaires 2025/C/47 en 2025/C/48 geven de uitvoering.</p>
<p>Voor gewone renovatie, waaronder dakwerken aan een woning ouder dan tien jaar, is geen wijziging van de leeftijdsgrens gevonden.</p>
<div class="note">Btw-regels wijzigen vaker dan bouwregels. De actuele tekst staat bij de FOD Financien op https://financien.belgium.be en bij de beroepsfederaties.</div>

<h2>Wat niet onder 6 procent valt</h2>
<p>Leveringen zonder plaatsing, werk aan gebouwen jonger dan tien jaar, en werk aan gedeelten die niet als woning worden gebruikt. Bij gemengd gebruik wordt opgesplitst.</p>
%s""" % sources([
           "Embuild over de afschaffing van het btw-attest en de vervanging door een verklaring op de factuur: https://embuild.be/nl/afschaffing-attest-bij-renovatie-aan-6-btw-sterke-administratieve-vereenvoudiging-voor-consument-en",
           "Bouwunie over de nieuwe btw-regels in het Belgisch Staatsblad: https://www.bouwunie.be/nl/nieuws/nieuwe-btwregels-gepubliceerd-in-het-belgisch-staatsblad",
           "FOD Financien over btw van 6 procent bij afbraak en heropbouw: https://financien.belgium.be/nl/programmawet/btw-6procent-afbraak-heropbouw",
       ]))

    _p("epc-renovatieverplichting", "EPC en de renovatieverplichting",
       "Woningen met label E of F naar minimaal label D binnen zes jaar na de akte, met de boetevork en de afgeschafte verstrenging.",
       """<h1>EPC en de renovatieverplichting</h1>
<p class="lead">Sinds 1 januari 2023 geldt in Vlaanderen een renovatieverplichting voor residentiele gebouwen. Wie een woning koopt met een slecht EPC-label, moet die binnen een vaste termijn verbeteren.</p>

<h2>Wat geldt in 2026</h2>
<ul>
<li>Woningen met EPC-label E of F moeten worden gerenoveerd naar minimaal label D.</li>
<li>De termijn is zes jaar na de authentieke akte. Die verlenging van vijf naar zes jaar werd definitief goedgekeurd op 12 december 2025 en geldt zowel voor lopende als voor nieuwe overdrachten.</li>
<li>Het verstrengingspad dat vanaf 2028 was gepland, met label C in 2028 en label B en A in latere jaren, is afgeschaft.</li>
<li>De boete voor residentiele gebouweenheden bedraagt 500 tot 5.000 euro, in plaats van de eerdere vork tot 200.000 euro. Een boete heft de verplichting niet op; er volgt onmiddellijk een nieuwe termijn.</li>
</ul>

<h2>De rol van het dak</h2>
<p>Het dak is de grootste post in de gebouwschil. Bij een woning zonder dakisolatie levert isoleren van het dak doorgaans de grootste labelsprong per geinvesteerde euro. De Woningpas hanteert als richtwaarde dat een goed geisoleerd dak minstens 7 centimeter PUR of 9 centimeter minerale wol bevat, en dat de energiedoelstelling 2050 uitkomt op een U-waarde van 0,24 watt per vierkante meter kelvin, ongeveer 12 centimeter PUR of 14 centimeter minerale wol.</p>

<h2>Volgorde bij een aankoop met label E of F</h2>
<ol>
<li>Het EPC-verslag lezen. Daarin staat welke onderdelen als niet-geisoleerd zijn ingeschat.</li>
<li>Nagaan of het dak toegankelijk is en of de dakbedekking op korte termijn toch vervangen moet worden.</li>
<li>Isolatie en dakvernieuwing samen aanbesteden wanneer beide nodig zijn.</li>
<li>Na de werken een nieuw EPC laten opmaken, want alleen dat telt als bewijs.</li>
</ol>
%s""" % sources([
           "Vlaanderen over de renovatieverplichting voor residentiele gebouwen: https://www.vlaanderen.be/bouwen-wonen-en-energie/kopen-en-verkopen/een-huis-of-appartement-kopen/renovatieverplichting-voor-residentiele-gebouwen",
           "Woningpas over dakisolatie: https://woningpas.vlaanderen.be/web/woningkwaliteit/energiezuinige-woning/aan-de-slag/dakisolatie",
       ]))
