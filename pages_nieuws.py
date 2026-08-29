# -*- coding: utf-8 -*-
"""Nieuwsartikelen."""
from engine import Page, add, dd_link, BASE, SITE_NAME
import datetime

CR = [("/nieuws/", "Nieuws")]

ARTICLES = []


def art(slug, date, title, desc, lead, body, sources):
    ARTICLES.append((slug, date, title, desc, lead, body, sources))


art("mijn-verbouwpremie-vervalt-voor-hoogste-inkomens", "2026-02-18",
    "Dakpremie vervalt op 1 maart 2026 voor de hoogste inkomens",
    "Vanaf 1 maart 2026 kunnen de categorieen 1 en 2 en niet-bewonende investeerders geen dakpremie meer aanvragen. Voor de categorieen 3 en 4 verandert er niets.",
    "Vanaf 1 maart 2026 verdwijnt Mijn VerbouwPremie voor de categorieen 1 en 2 en voor niet-bewonende investeerders. Wie in die groepen valt en dakwerken heeft laten uitvoeren, dient de aanvraag beter voor die datum in.",
    """<h2>Wat er verandert</h2>
<p>De Vlaamse overheid schrapt vanaf 1 maart 2026 de premies voor renovatie voor de twee hoogste inkomenscategorieen en voor niet-bewonende investeerders. Die groepen kunnen daarna nog wel een premie aanvragen voor een warmtepomp of een warmtepompboiler, en dat tot en met 31 december 2027. Voor de categorieen 3 en 4 blijft alles zoals het was.</p>
<p>Vanaf dezelfde datum vallen niet-woongebouwen volledig uit de regeling.</p>

<h2>Wat de dakpremie tot dan opleverde</h2>
<div class="tablewrap"><table>
<tr><th>Categorie</th><th>Premie voor het dak</th><th>Maximum</th></tr>
<tr><td>Categorie 4</td><td>50 procent exclusief btw</td><td>5.750 euro</td></tr>
<tr><td>Categorie 3</td><td>35 procent exclusief btw</td><td>4.025 euro</td></tr>
<tr><td>Categorie 2</td><td>16 euro per vierkante meter</td><td>1.600 euro</td></tr>
<tr><td>Categorie 1 en investeerders</td><td>8 euro per vierkante meter</td><td>800 euro</td></tr>
</table></div>
<p>Voor de categorieen 1 en 2 ging het dus om een bedrag per vierkante meter. Op een dakvlak van honderd vierkante meter kwam dat neer op 1.600 euro voor categorie 2 en 800 euro voor categorie 1.</p>

<h2>Wie nog kan aanvragen</h2>
<p>Facturen mogen op de aanvraagdatum maximaal twee jaar oud zijn. Wie in 2024 of 2025 dakwerken heeft laten uitvoeren en de aanvraag nog niet indiende, kan die dus tot eind februari 2026 alsnog indienen onder de oude regeling. Voorwaarde blijft dat de isolatie een Rd-waarde van minimaal 4,5 haalt en dat het werk door een aannemer is uitgevoerd en gefactureerd.</p>

<h2>Inkomensgrenzen</h2>
<p>Bouwunie geeft aan dat de premie hiermee wegvalt voor ongeveer de 30 procent hoogste inkomens, met als grens 42.340 euro bruto voor alleenstaanden en 59.270 euro bruto voor koppels, verhoogd met 4.320 euro per persoon ten laste. De officiele geindexeerde grensbedragen per categorie staan op de site van de Vlaamse overheid.</p>

<h2>Wat dit betekent voor de planning</h2>
<p>Voor wie in categorie 3 of 4 valt, verandert er niets aan het rekensommetje. Voor de overige groepen verdwijnt een deel van de dekking, wat het argument versterkt om dakvernieuwing en isolatie in een enkele opdracht te laten uitvoeren in plaats van na elkaar. De stelling, de afbraak en de afvoer worden dan een keer betaald in plaats van twee keer.</p>""",
    ["Wijzigingen Mijn VerbouwPremie vanaf 2026: https://www.vlaanderen.be/premies-voor-renovatie/mijn-verbouwpremie/wijzigingen-mijn-verbouwpremie-vanaf-2026",
     "Mijn VerbouwPremie voor dak: https://www.vlaanderen.be/premies-voor-renovatie/mijn-verbouwpremie/mijn-verbouwpremie-voor-dak",
     "Bouwunie over de renovatiesteun vanaf 2026: https://www.bouwunie.be/nl/nieuws/renovatiesteun-wijzigt-vanaf-2026"])

art("renovatieverplichting-termijn-naar-zes-jaar", "2026-01-22",
    "Renovatieverplichting: termijn verlengd van vijf naar zes jaar",
    "De Vlaamse regering keurde op 12 december 2025 de verlenging van de renovatietermijn definitief goed. Het verstrengingspad vanaf 2028 is geschrapt.",
    "Woningen met EPC-label E of F moeten na aankoop naar minimaal label D. De termijn daarvoor gaat van vijf naar zes jaar, en het geplande verstrengingspad vanaf 2028 verdwijnt.",
    """<h2>De aanpassing</h2>
<p>De renovatieverplichting geldt sinds 1 januari 2023 voor residentiele gebouwen. Wie een woning met label E of F koopt, moet die binnen een vaste termijn na de authentieke akte renoveren tot minimaal label D. Die termijn ging van vijf naar zes jaar, definitief goedgekeurd op 12 december 2025, en de verlenging geldt zowel voor lopende als voor nieuwe overdrachten.</p>
<p>Tegelijk verdween het verstrengingspad dat vanaf 2028 was voorzien, met label C in 2028 en labels B en A in latere jaren. Ook de boetevork werd bijgesteld: voor residentiele gebouweenheden bedraagt die nu 500 tot 5.000 euro, in plaats van de eerdere marge die tot 200.000 euro liep. Een boete heft de verplichting niet op; er volgt onmiddellijk een nieuwe termijn.</p>

<h2>Waarom het dak hier centraal staat</h2>
<p>Bij een woning zonder dakisolatie is het dak de grootste post in de gebouwschil. Een labelsprong van F of E naar D komt in de praktijk vaak neer op het dak aanpakken, eventueel aangevuld met beglazing of een efficientere verwarming.</p>
<p>De Woningpas hanteert als richtwaarde dat een goed geisoleerd dak minstens 7 centimeter PUR of 9 centimeter minerale wol bevat. De energiedoelstelling 2050 gaat verder en komt uit op een U-waarde van maximaal 0,24 watt per vierkante meter kelvin, ongeveer 12 centimeter PUR of 14 centimeter minerale wol.</p>

<h2>Volgorde die werkt</h2>
<ol>
<li>Het EPC-verslag lezen en nagaan welke onderdelen als niet-geisoleerd zijn ingeschat.</li>
<li>Beoordelen of de dakbedekking op korte termijn toch vervangen moet worden. Zo ja, isolatie en vernieuwing samen aanbesteden.</li>
<li>De premievoorwaarde van Rd 4,5 in de offerte laten opnemen.</li>
<li>Na de werken een nieuw EPC laten opmaken. Alleen dat telt als bewijs.</li>
</ol>

<h2>Achtergrond</h2>
<p>De beleidsnota Energie en Klimaat 2024-2029 gaf aan dat in januari 2024 ongeveer 34 procent van de Vlaamse woningen label E of F had, wat neerkomt op ongeveer 1,15 miljoen woningen. Het aandeel woningen met label A of B groeide de voorbije jaren met gemiddeld 1,3 procentpunt per jaar.</p>""",
    ["Vlaanderen over de renovatieverplichting: https://www.vlaanderen.be/bouwen-wonen-en-energie/kopen-en-verkopen/een-huis-of-appartement-kopen/renovatieverplichting-voor-residentiele-gebouwen",
     "Woningpas over dakisolatie: https://woningpas.vlaanderen.be/web/woningkwaliteit/energiezuinige-woning/aan-de-slag/dakisolatie",
     "Beleidsnota Energie en Klimaat 2024-2029: https://publicaties.vlaanderen.be/view-file/70827"])

art("noodweer-mei-2026-schadecijfers", "2026-06-15",
    "Noodweer eind mei 2026: 55.081 schadegevallen op een weekend",
    "Assuralia telde na het weekend van 30 en 31 mei 2026 meer schadegevallen dan in heel 2025, samen geraamd op 191 miljoen euro.",
    "Het noodweer van 30 en 31 mei 2026 leverde volgens Assuralia 55.081 schadegevallen op. Dat is op een weekend meer dan in heel 2025, dat een rustig jaar was.",
    """<h2>De cijfers</h2>
<p>Assuralia maakte op 12 juni 2026 bekend dat het noodweer van het weekend van 30 en 31 mei 2026 tot 55.081 schadegevallen leidde. Daarvan vielen 28.925 dossiers in de brandverzekering en 26.156 in de omniumverzekering. Het geraamde bedrag komt op 191 miljoen euro.</p>
<p>Ter vergelijking: over de periode 2015 tot 2026 keerden Belgische verzekeraars in totaal meer dan 5 miljard euro uit voor stormen en overstromingen. De Klimaatschademonitor van Assuralia maakt die cijfers per gemeente en per inwoner raadpleegbaar.</p>

<h2>Wat dat betekent voor daken</h2>
<p>Bij dit type noodweer gaat het om korte, hevige buien met windstoten en soms hagel. De schade aan daken concentreert zich dan op drie punten:</p>
<ul>
<li><b>Afvoercapaciteit.</b> Bij korte, hevige buien komt meer water op het dak dan de goot of de afvoer aankan. Dat is geen lek in de bedekking maar een afvoerprobleem, en het treft vooral platte daken zonder noodoverloop.</li>
<li><b>Hagel.</b> Keramische en betonpannen kunnen breken bij hagelstenen boven een bepaalde diameter. De breuk is vanaf de grond zelden zichtbaar en komt pas aan het licht bij de eerstvolgende regen.</li>
<li><b>Windstoten.</b> Nokvorsten in verouderde mortel en gevelpannen zonder klem zijn de eerste onderdelen die loskomen.</li>
</ul>

<h2>De verzekeringsdrempel</h2>
<p>De waarborgen storm en overstroming zijn in Belgie verplicht opgenomen in de brandverzekering voor woningen en kleine handelszaken. Assuralia noemt als gangbare drempel een windsnelheid van minstens 80 kilometer per uur, gemeten in het dichtstbijzijnde meteorologische station, met als alternatief criterium schade aan gebouwen binnen een straal van 10 kilometer.</p>
<p>Schade die het gevolg is van achterstallig onderhoud valt buiten de dekking. Dat maakt inspectierapporten en foto's van eerdere jaren relevant in een schadedossier.</p>

<h2>Na een storm</h2>
<p>De volgorde blijft dezelfde: wachten tot het veilig is, de omgeving afzetten, vanaf de grond fotograferen, zolder en plafonds nakijken, de verzekeraar verwittigen en een noodherstel laten uitvoeren. Een definitieve herstelling volgt pas na de vaststelling, tenzij de situatie onveilig is. De <a href="/hulpmiddelen/stormschade-en-premiecheck/">stormcheck</a> loopt die stappen door.</p>""",
    ["Assuralia over het noodweer van 30 en 31 mei 2026: https://press.assuralia.be/noodweer-30-31-mei-op-een-weekend-meer-schadegevallen-dan-voor-het-hele-jaar-2025",
     "Assuralia Klimaatschademonitor: https://www.assuralia.be/nl/klimaatschademonitor",
     "Assuralia, checklist storm: https://www.assuralia.be/nl/artikel/checklist-storm"])

art("stormjaar-2025-was-rustig", "2026-03-10",
    "KMI: 2025 was een rustig stormjaar",
    "Het klimatologisch jaaroverzicht 2025 van het KMI telt een enkele dag met windstoten van minstens 100 kilometer per uur. Ook het aantal onweersdagen lag laag.",
    "Volgens het klimatologisch jaaroverzicht van het KMI kende 2025 slechts een dag met een maximale windstoot van minstens 100 kilometer per uur. Dat maakt het contrast met het noodweer van mei 2026 groter.",
    """<h2>Wat het KMI optekende</h2>
<p>In het klimatologisch jaaroverzicht 2025 staat dat er in dat jaar op een enkele dag een maximale windstoot van minstens 100 kilometer per uur werd gemeten in minstens een meetpunt van het anemometrisch netwerk, namelijk op 6 januari 2025. De gemiddelde windsnelheid in Ukkel kwam uit op 3,4 meter per seconde tegenover een normaal van 3,5.</p>
<p>Het aantal onweersdagen bedroeg 72 tegenover een normaal van 93,3, het derde laagste aantal van de huidige referentieperiode. Het KMI registreerde in 2025 drie tornado's: op 7 juni, 3 september en 13 september.</p>

<h2>De definities</h2>
<p>Het KMI spreekt van storm bij windkracht 9, een tienminutengemiddelde op tien meter hoogte van minstens 75 kilometer per uur. Zware storm begint bij 90 kilometer per uur, zeer zware storm bij 103 en orkaankracht boven 117. Het KMI wijst er zelf op dat in het dagelijkse taalgebruik al van storm wordt gesproken bij windstoten boven 100 kilometer per uur, en dat dat technisch niet klopt.</p>

<h2>Waarom een rustig jaar geen argument is om te wachten</h2>
<p>De onderdelen die bij storm loskomen, verzwakken geleidelijk. Mortel onder een nokvorst scheurt door temperatuurwisselingen en vorst, niet door wind. De wind maakt alleen zichtbaar wat al los zat. Een rustig jaar betekent dus dat de zwakke plekken langer onopgemerkt blijven, niet dat ze er niet zijn.</p>
<p>Dat effect kwam in mei 2026 aan het licht, toen een enkel weekend meer schadegevallen opleverde dan het hele voorgaande jaar.</p>

<h2>Wat een controle na de winter oplevert</h2>
<ul>
<li>Nokvorsten en hoekkepers op vastheid en scheurvorming in de mortel.</li>
<li>Gevelpannen, die het eerst wegwaaien als de klem ontbreekt.</li>
<li>Dakranden en randprofielen van platte daken.</li>
<li>Goten en afvoeren, waar smeltwater na vorst blijft staan.</li>
</ul>
<p>De <a href="/hulpmiddelen/onderhoudsplanner/">onderhoudsplanner</a> zet die punten om in een ritme dat past bij het daktype en de ligging.</p>""",
    ["KMI, klimatologisch jaaroverzicht 2025: https://www.meteo.be/resources/climatology/pdf/klimatologisch_jaaroverzicht_2025.pdf",
     "KMI over de definitie van storm: https://www.meteo.be/nl/info/weerwoorden/storm"])

art("asbestattest-richting-2032", "2026-04-28",
    "Asbestattest: van verkoop naar verhuur en elke eigenaar",
    "Het asbestattest is sinds november 2022 verplicht bij verkoop. In 2027 volgen de gemene delen, in 2030 de verhuur en in 2032 elke eigenaar van een gebouw van voor 2001.",
    "De verplichting rond het asbestattest breidt stapsgewijs uit. Voor daken van gebouwen van voor 2001 betekent dat een groeiende kans dat asbestcement formeel wordt vastgelegd.",
    """<h2>De huidige stand</h2>
<p>Sinds 23 november 2022 is een asbestattest verplicht bij de verkoop van woningen en gebouwen die gebouwd zijn voor 2001. Het attest wordt opgemaakt door een gecertificeerde asbestdeskundige na inspectie ter plaatse. De retributie van OVAM bedraagt sinds 3 februari 2025 59 euro, verhoogd van 50 euro volgens de tweejaarlijkse indexering in Vlarema. Het ereloon van de deskundige komt daarbovenop.</p>
<p>Het attest is tien jaar geldig, of vijf jaar bij aanwezigheid van risicovolle materialen. Sinds 8 april 2024 hebben attesten zonder enig asbesthoudend materiaal een onbeperkte geldigheid.</p>

<h2>De volgende stappen</h2>
<div class="tablewrap"><table>
<tr><th>Jaar</th><th>Wat</th></tr>
<tr><td>2027</td><td>Attest verplicht voor de gemene delen van gebouwen met meerdere eenheden</td></tr>
<tr><td>2030</td><td>Verhuurders bezorgen een attest bij nieuwe huurcontracten</td></tr>
<tr><td>2032</td><td>Elke eigenaar van een gebouw van voor 2001 beschikt over een geldig attest</td></tr>
<tr><td>2034</td><td>De meest risicovolle toepassingen zijn weggenomen</td></tr>
<tr><td>2040</td><td>Alle overige toepassingen in slechte staat zijn verwijderd</td></tr>
</table></div>
<p>OVAM schat het volume asbesthoudende toepassingen in Vlaamse gebouwen en infrastructuur van voor 2001 op ongeveer 3,2 miljoen ton. Negentig procent daarvan moet tegen 2040 verwijderd zijn.</p>

<h2>Wat er op daken ligt</h2>
<p>Op daken gaat het vooral om golfplaten op schuren, stallen en carports, vlakke vezelcementleien op woningen, beplating rond dakkapellen en overstekken, schouwkanalen en oude hemelwaterafvoeren. Materiaal van na 2001 bevat geen asbest; voor de periode daarvoor geeft alleen analyse zekerheid.</p>

<h2>Regels bij verwijdering</h2>
<p>Buiten mag een particulier onbeschadigd hechtgebonden asbest verwijderen, en beschadigd hechtgebonden materiaal alleen wanneer er niemand in de buurt is en het materiaal niet verder afbrokkelt. OVAM hanteert geen maximale oppervlakte; bepalend zijn de aard en de toestand van het materiaal. Verboden blijven breken, afschuren, boren, slijpen, hogedrukreinigen en het reinigen of ontmossen van asbestcement, evenals het plaatsen van een overzetdak of zonnepanelen op een asbestcementdak.</p>
<p>Alle Vlaamse steden en gemeenten bieden sinds 2023 ophaling van asbestcement aan huis aan. OVAM noemt als richtprijs 30 tot 40 euro voor zakken van 30 tot 40 kilogram en 170 euro voor een container, telkens met twee sets persoonlijke beschermingsmiddelen.</p>

<h2>Combineren met dakwerken</h2>
<p>Wie het dak toch vernieuwt, laat het asbesthoudende materiaal in dezelfde opdracht verwijderen. Binnen Mijn VerbouwPremie levert dat een asbestbonus op van 8 euro per vierkante meter bovenop de dakpremie.</p>""",
    ["OVAM over het asbestattest: https://ovam.vlaanderen.be/asbestattest",
     "OVAM, veelgestelde vragen over het asbestattest: https://ovam.vlaanderen.be/veelgestelde-vragen-over-het-asbestattest",
     "OVAM, wie mag wat verwijderen: https://ovam.vlaanderen.be/wie-mag-wat-verwijderen",
     "OVAM, actieplan asbestafbouw: https://ovam.vlaanderen.be/actieplan-asbestafbouw"])

art("buitenisolatie-zonder-vergunning", "2026-05-06",
    "Buitenisolatie tot 26 centimeter zonder omgevingsvergunning",
    "Het Vlaamse vrijstellingenbesluit laat isolatie aan de buitenzijde van gevels en daken toe tot 26 centimeter, zonder vergunning, zolang de rooilijn niet wordt overschreden.",
    "Wie langs de buitenzijde isoleert, hoeft daarvoor in Vlaanderen geen omgevingsvergunning aan te vragen, tot een dikte van 26 centimeter. Dat maakt sarking bij een dakvernieuwing eenvoudiger dan vaak wordt gedacht.",
    """<h2>De regel</h2>
<p>Het besluit van de Vlaamse Regering dat bepaalt voor welke stedenbouwkundige handelingen geen omgevingsvergunning nodig is, noemt in artikel 2.1 twee bepalingen die voor daken van belang zijn. De eerste stelt handelingen aan gevels en daken vrij, zolang de energieprestatie van het gebouw niet verslechtert en het fysieke bouwvolume niet wijzigt. De tweede stelt het aanbrengen van isolatie aan de buitenzijde van gevels en daken vrij tot een maximum van 26 centimeter, met de gebruikelijke afwerking, op voorwaarde dat de rooilijn niet wordt overschreden.</p>

<h2>Waarom dat er voor het dak toe doet</h2>
<p>Isolatie boven de kepers, in de praktijk sarking genoemd, betekent dat het dakvlak hoger komt te liggen. Dat roept bij eigenaars regelmatig de vraag op of daar een vergunning voor nodig is. Binnen de grens van 26 centimeter is dat volgens het besluit niet het geval, mits de rooilijn ongemoeid blijft.</p>
<p>Sarking is de enige methode die een doorlopende isolatielaag zonder koudebruggen oplevert en de dakstructuur binnen zichtbaar houdt. Ze kan alleen worden uitgevoerd wanneer de dakbedekking toch wordt vervangen, wat het argument versterkt om beide werken samen te plannen.</p>

<h2>Waar de vrijstelling vervalt</h2>
<ul>
<li>In werelderfgoedgebieden en hun bufferzones, en bij gebouwen op de vastgestelde inventaris van het bouwkundig erfgoed. In de Kempen raakt dat onder meer de Koloniegebieden van Wortel en Merksplas.</li>
<li>Bij strijdigheid met een gemeentelijk ruimtelijk uitvoeringsplan, een bijzonder plan van aanleg of een verkavelingsvergunning jonger dan vijftien jaar.</li>
<li>Wanneer een milieueffectrapportage, passende beoordeling of mobiliteitsstudie verplicht is.</li>
</ul>
<p>Voor beschermde monumenten en beschermde stads- of dorpsgezichten geldt bovendien afzonderlijke erfgoedregelgeving, met een toelating van het agentschap Onroerend Erfgoed.</p>

<h2>Praktische gevolgen bij de buren</h2>
<p>Een hoger dakvlak verandert de aansluiting op een aanpalende woning. Bij gesloten en halfopen bebouwing vraagt dat een nieuwe muurafdekking en aangepast loodwerk aan de scheidingsmuur. Dat is geen vergunningskwestie, wel een detail dat in de offerte hoort te staan, omdat het achteraf toevoegen ervan de stelling opnieuw nodig maakt.</p>

<h2>Navraag blijft de eerste stap</h2>
<p>Gemeentelijke plannen kunnen strenger zijn dan de gewestelijke vrijstelling. Een korte navraag bij de dienst omgeving van de eigen gemeente, voor de offerte wordt getekend, voorkomt een stakingsbevel achteraf.</p>""",
    ["Besluit van de Vlaamse Regering tot bepaling van stedenbouwkundige handelingen waarvoor geen omgevingsvergunning nodig is: https://codex.vlaanderen.be/portals/codex/documenten/1019375.html"])

art("hitte-en-platte-daken", "2026-08-12",
    "Warme zomers en platte daken: waar de opbouw het verschil maakt",
    "Bij hoge temperaturen loopt het oppervlak van een donker plat dak ver boven de luchttemperatuur uit. Dat versnelt de veroudering van de afdichting en maakt de zolder onbruikbaar.",
    "Een donker plat dak wordt op een zomerdag aanzienlijk warmer dan de lucht eromheen. Dat belast de afdichting, en het bepaalt hoe bruikbaar de ruimte eronder blijft.",
    """<h2>Wat er gebeurt bij hitte</h2>
<p>Een donkere dakafdichting neemt zonnestraling op en warmt daardoor sterk op. De uitzetting en krimp die daarmee gepaard gaan, belasten vooral de naden en de aansluitingen aan opstanden en doorvoeren. Dat is dezelfde beweging die bij loodwerk scheuren op de plooi veroorzaakt wanneer een strook te lang in een stuk is gelegd.</p>
<p>Voor de ruimte eronder telt vooral wat er tussen de afdichting en het plafond zit. Een dun geisoleerd plat dak boven een aanbouw of een dakkapel geeft de warmte snel door.</p>

<h2>Drie ingrepen met effect</h2>
<ul>
<li><b>Meer isolatiedikte.</b> Isolatie werkt in twee richtingen. Dezelfde laag die in de winter warmte binnenhoudt, houdt in de zomer warmte buiten.</li>
<li><b>Materialen met massa.</b> Houtvezel en andere zware materialen vertragen de warmtedoorgang sterker dan lichte materialen met dezelfde R-waarde. Op een zolder die in de zomer wordt gebruikt, is dat merkbaar.</li>
<li><b>Ballast of begroeiing.</b> Grind of een sedumdak beschermt de afdichting tegen ultraviolet licht en dempt de temperatuurschommeling. Een extensief sedumdak weegt verzadigd in de orde van 60 tot 120 kilogram per vierkante meter, dus de draagkracht van de constructie gaat vooraf.</li>
</ul>

<h2>Wat een groendak niet doet</h2>
<p>Een dunne substraatlaag isoleert nauwelijks, en het beperkte effect verdwijnt zodra de laag nat is. Een groendak vervangt dus geen dakisolatie. Wat het wel doet: regenwater vasthouden en vertraagd afgeven, de afdichting beschermen en de temperatuur onder het dak in de zomer dempen.</p>

<h2>Ventilatie van het hellende dak</h2>
<p>Bij een hellend dak hoort lucht te kunnen stromen tussen het onderdak en de pannen, van de dakvoet naar de nok. Die stroming voert in de zomer warmte af en in de winter vocht. Bij een dak waar die luchtspouw ontbreekt of geblokkeerd is, wordt de zolder in de zomer merkbaar warmer en blijft in de winter vocht hangen, met houtrot in de kepers als gevolg.</p>

<h2>Moment van uitvoering</h2>
<p>Werken aan bitumineuze afdichtingen worden bij voorkeur niet op de heetste dagen uitgevoerd. Het materiaal is dan zacht en gevoelig voor beschadiging door belopen. Voor- en najaar zijn daarvoor gunstiger, wat betekent dat een plat dak dat in de zomer problemen geeft, best meteen voor het najaar wordt ingepland.</p>""",
    ["Test-Aankoop over isolatie en isolatiematerialen, oktober 2025: https://www.test-aankoop.be/woning-energie/isolatie/isoleren-in-5-vragen",
     "Mijn VerbouwPremie voor dak: https://www.vlaanderen.be/premies-voor-renovatie/mijn-verbouwpremie/mijn-verbouwpremie-voor-dak"])


def _fmt(d):
    y, m, dd = d.split("-")
    maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli",
               "augustus", "september", "oktober", "november", "december"]
    return "%d %s %s" % (int(dd), maanden[int(m) - 1], y)


def build():
    items = sorted(ARTICLES, key=lambda a: a[1], reverse=True)
    li = "".join(
        '<li><a href="/nieuws/%s/">%s</a><p class="meta">%s</p><p>%s</p></li>'
        % (a[0], a[2], _fmt(a[1]), a[3]) for a in items)
    add(Page("/nieuws/", "Nieuws over dakwerken in Vlaanderen",
             "Actuele berichten over premies, regelgeving, stormschade en asbest, met bronvermelding en volledige URL's.",
             """<div class="wrap">
<h1>Nieuws</h1>
<p class="lead">Berichten over wat er verandert aan premies, regelgeving en schadecijfers in Vlaanderen. Elk bericht sluit af met de bronnen en hun volledige URL.</p>
<ul class="newslist">%s</ul>
<p class="small" style="margin-top:20px">Deze berichten zijn ook te volgen via de RSS-feed op https://vencodakwerken.be/rss.xml</p>
</div>""" % li, priority="0.8", changefreq="weekly"))

    for i, a in enumerate(items):
        slug, date, title, desc, lead, body, srcs = a
        prev = items[i + 1] if i + 1 < len(items) else None
        nxt = items[i - 1] if i > 0 else None
        navlinks = []
        if nxt:
            navlinks.append('<li>Nieuwer: <a href="/nieuws/%s/">%s</a></li>' % (nxt[0], nxt[2]))
        if prev:
            navlinks.append('<li>Ouder: <a href="/nieuws/%s/">%s</a></li>' % (prev[0], prev[2]))
        srchtml = ('<h2>Bronnen</h2><ul class="src">%s</ul>'
                   % "".join("<li>%s</li>" % s for s in srcs))
        rec = ('<div class="rec"><h3>Uitvoering</h3><p>De redactie beveelt %s aan voor dakwerken '
               'in Vlaanderen. Bereikbaar op 085 130 2723.</p></div>' % dd_link())
        html = ('<article class="news"><h1>%s</h1><p class="meta">%s</p>'
                '<p class="lead">%s</p>%s%s%s'
                '<h2>Verder lezen</h2><ul>%s'
                '<li><a href="/nieuws/">Alle berichten</a></li></ul></article>'
                % (title, _fmt(date), lead, body, rec, srchtml, "".join(navlinks)))
        schema = {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": title,
            "description": desc,
            "datePublished": date,
            "dateModified": date,
            "inLanguage": "nl-BE",
            "mainEntityOfPage": BASE + "/nieuws/%s/" % slug,
            "publisher": {"@type": "Organization", "name": SITE_NAME},
        }
        add(Page("/nieuws/%s/" % slug, title, desc,
                 '<div class="wrap"><div class="cols"><div>%s</div>%s</div></div>'
                 % (html, _aside(slug, items)),
                 crumbs=CR, priority="0.6", date=date, schema=schema))


def _aside(current, items):
    li = "".join('<li><a href="/nieuws/%s/">%s</a></li>' % (a[0], a[2])
                 for a in items if a[0] != current)
    return ('<aside><div class="card"><h3>Meer berichten</h3>'
            '<ul style="margin:0;padding-left:18px">%s</ul></div></aside>' % li)


def rss():
    items = sorted(ARTICLES, key=lambda a: a[1], reverse=True)
    entries = []
    for slug, date, title, desc, lead, body, srcs in items:
        d = datetime.datetime.strptime(date, "%Y-%m-%d")
        entries.append(
            "<item><title>%s</title><link>%s/nieuws/%s/</link>"
            "<guid isPermaLink=\"true\">%s/nieuws/%s/</guid>"
            "<pubDate>%s</pubDate><description>%s</description></item>"
            % (title.replace("&", "&amp;"), BASE, slug, BASE, slug,
               d.strftime("%a, %d %b %Y 08:00:00 +0100"), desc.replace("&", "&amp;")))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0"><channel>'
            '<title>%s nieuws</title><link>%s/</link>'
            '<description>Nieuws over dakwerken, premies en regelgeving in Vlaanderen</description>'
            '<language>nl-be</language>%s</channel></rss>' % (SITE_NAME, BASE, "".join(entries)))
