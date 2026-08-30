# -*- coding: utf-8 -*-
"""De gids: twaalf hoofdstukken over dakwerken in Vlaanderen."""
from engine import Page, add, dd_link, dd_url

CR = [("/dakwerken/", "Dakwerken")]


def rec(text, path="", anchor=None):
    return ('<div class="rec"><h3>Uitvoering</h3><p>%s</p>'
            '<p>Aanbevolen uitvoerder: %s, 085 130 2723.</p></div>'
            % (text, dd_link(path, anchor)))


def sources(items):
    li = "".join("<li>%s</li>" % i for i in items)
    return ('<h2>Bronnen</h2><ul class="src">%s</ul>' % li)


CHAPTERS = [
    ("hellend-dak", "Hellend dak", "Pannen, leien en de opbouw eronder"),
    ("plat-dak", "Plat dak", "Roofing, EPDM en de opbouw van een warm dak"),
    ("dakisolatie", "Dakisolatie", "R-waarden, methodes en de norm in Vlaanderen"),
    ("daklekkage", "Daklekkage", "Oorzaken opsporen en de schade beperken"),
    ("dakgoot", "Dakgoot en regenafvoer", "Hanggoot, bakgoot en afvoer"),
    ("schouw", "Schouw en dakdoorvoeren", "Voegwerk, loodslabben en doorvoeren"),
    ("zink-en-loodwerk", "Zink- en loodwerk", "Kilgoten, muuraansluitingen en slabben"),
    ("dakramen-en-dakkapel", "Dakramen en dakkapel", "Licht op zolder zonder lekrisico"),
    ("groendak", "Groendak", "Sedum, opbouw en draagkracht"),
    ("asbest-op-het-dak", "Asbest op het dak", "Herkennen, regels en verwijdering"),
    ("dakonderhoud", "Dakonderhoud", "Wat wanneer nagekeken hoort te worden"),
    ("stormschade", "Stormschade", "Direct handelen, verzekering en herstel"),
]


def build():
    tiles = "".join(
        '<a class="tile" href="/dakwerken/%s/"><b>%s</b><span>%s</span></a>' % (s, t, d)
        for s, t, d in CHAPTERS)
    add(Page(
        "/dakwerken/",
        "Dakwerken in Vlaanderen: de volledige gids",
        "Twaalf hoofdstukken over hellende en platte daken, isolatie, lekkage, goten, schouwen, asbest en onderhoud, toegespitst op de Vlaamse regelgeving.",
        """<div class="wrap">
<h1>Dakwerken in Vlaanderen</h1>
<p class="lead">Deze gids behandelt de twaalf onderwerpen waar de meeste dakvragen onder vallen. Elk hoofdstuk beschrijft hoe het onderdeel werkt, wat er misgaat, wat een correcte oplossing inhoudt en welke Vlaamse regels van toepassing zijn.</p>
<div class="grid">%s</div>
<h2>Volgorde van aanpak</h2>
<p>Wie voor het eerst met een dakprobleem te maken krijgt, volgt best deze volgorde. Eerst vaststellen of het om een acuut lek gaat of om slijtage. Vervolgens bepalen of herstel volstaat of dat het volledige dakvlak aan vervanging toe is. Pas daarna komt de vraag naar isolatie, premies en vergunningen aan bod, omdat die keuzes de uitvoering en de kostprijs sterk beinvloeden.</p>
<p>Een dakvernieuwing die samenvalt met isolatiewerk levert een aanzienlijk hogere premie op dan losse ingrepen na elkaar. Wie het dak toch openlegt, isoleert in dezelfde beweging. Meer daarover staat op <a href="/regelgeving/mijn-verbouwpremie/">de pagina over Mijn VerbouwPremie</a>.</p>
%s
</div>""" % (tiles, rec("Een dakinspectie met beeldmateriaal maakt duidelijk of herstel volstaat of dat vervanging nodig is.", "dakinspectie/", "dendekker-dakbedekking.nl/dakinspectie/")),
        crumbs=[], priority="0.8"))

    _hellend()
    _plat()
    _isolatie()
    _lekkage()
    _goot()
    _schouw()
    _zink()
    _dakramen()
    _groendak()
    _asbest()
    _onderhoud()
    _storm()


def _p(slug, title, desc, body, prio="0.7"):
    add(Page("/dakwerken/%s/" % slug, title, desc,
             '<div class="wrap"><div class="cols"><div>%s</div>%s</div></div>' % (body, _aside(slug)),
             crumbs=CR, priority=prio))


def _aside(current):
    li = "".join('<li><a href="/dakwerken/%s/">%s</a></li>' % (s, t)
                 for s, t, _ in CHAPTERS if s != current)
    return ('<aside><div class="card"><h3>Andere hoofdstukken</h3>'
            '<ul style="margin:0;padding-left:18px">%s</ul>'
            '<p class="small" style="margin-top:14px"><a href="/hulpmiddelen/">Naar de hulpmiddelen</a></p>'
            '</div></aside>' % li)


def _hellend():
    _p("hellend-dak", "Hellend dak: pannen, leien en de opbouw eronder",
       "Hoe een hellend dak is opgebouwd, welke pannen en leien gangbaar zijn in Vlaanderen, wanneer herstel volstaat en wanneer het dakvlak vervangen moet worden.",
       """<h1>Hellend dak</h1>
<p class="lead">Het hellende dak is in Vlaanderen de meest voorkomende dakvorm bij woningen. De bedekking bestaat meestal uit keramische pannen, betonpannen of leien, gelegd op panlatten en tengellatten boven een onderdak.</p>

<h2>De opbouw van boven naar beneden</h2>
<ol>
<li>De dakbedekking: pannen of leien, die het meeste water afvoeren.</li>
<li>Panlatten, waarop de pannen haken.</li>
<li>Tengellatten, die een luchtspouw maken zodat water dat toch doorkomt naar beneden kan lopen.</li>
<li>Het onderdak: een folie of plaat die het resterende water opvangt en naar de goot afvoert. Bij woningen van voor 1970 ontbreekt dit vaak.</li>
<li>De isolatie, tussen of boven de kepers.</li>
<li>Het dampscherm aan de binnenzijde, dat vocht uit de woning tegenhoudt.</li>
<li>De afwerking, meestal gyproc of houten beplanking.</li>
</ol>
<p>Elke laag heeft een functie. Wie alleen de bovenste laag vervangt en de onderliggende opbouw laat zoals ze is, lost daarmee een lek zelden blijvend op.</p>

<h2>Materialen die in Vlaanderen gangbaar zijn</h2>
<div class="tablewrap"><table>
<tr><th>Materiaal</th><th>Kenmerk</th><th>Aandachtspunt</th></tr>
<tr><td>Keramische pan</td><td>Gebakken klei, kleurvast</td><td>Modellen verdwijnen uit productie, deelvervanging wordt lastiger</td></tr>
<tr><td>Betonpan</td><td>Zwaarder, gladder oppervlak</td><td>Verkleurt en vergroent sneller aan de noordzijde</td></tr>
<tr><td>Natuurleien</td><td>Dun, licht, lange staat van dienst</td><td>Vraagt vakkennis bij het haken en nagelen</td></tr>
<tr><td>Vezelcementleien</td><td>Goedkoper alternatief voor natuurlei</td><td>Bij bouwjaar voor 2001 mogelijk asbesthoudend</td></tr>
<tr><td>Riet</td><td>Traditioneel, hoge isolatiewaarde</td><td>Brandveiligheidseisen en specialistisch onderhoud</td></tr>
</table></div>

<h2>Wanneer herstel volstaat</h2>
<p>Herstel is zinvol wanneer de schade lokaal is en de onderliggende constructie droog en gaaf is. Voorbeelden: enkele gebroken pannen na hagel, een losgekomen nokvorst, een verschoven gevelpan. Een vakman vervangt dan alleen het beschadigde deel en controleert meteen de aansluitingen rondom.</p>

<h2>Wanneer vervanging nodig is</h2>
<p>Vervanging van het volledige dakvlak komt in beeld bij een combinatie van signalen: pannen die op meerdere plaatsen tegelijk breken, een onderdak dat verpulvert bij aanraking, panlatten met houtrot, terugkerende lekken op wisselende plaatsen, en het ontbreken van isolatie. In dat geval is losse reparatie na losse reparatie geen oplossing.</p>
<p>Een dakvernieuwing is ook het moment om de isolatie in orde te brengen. De werken zijn dan al opgezet en het dakvlak ligt open. Wie dat later apart laat doen, betaalt tweemaal voor stelling, afbraak en afvoer.</p>

<h2>Nokvorsten</h2>
<p>De nokvorsten sluiten het hoogste punt van het dak af. Traditioneel liggen ze in mortel. Die mortel scheurt na verloop van tijd door temperatuurwisselingen en vorst. Een poreuze of losse nokvorst laat water door en kan bij storm loskomen. De moderne oplossing is droge nokafwerking met een ventilerende nokrol en klemmen, waarbij geen mortel meer nodig is.</p>
%s

<h2>Ventilatie van het dakvlak</h2>
<p>Tussen het onderdak en de pannen hoort lucht te kunnen stromen, van de dakvoet naar de nok. Zonder die stroming blijft vocht hangen, wat leidt tot houtrot in de kepers en tot schimmel op de isolatie. Bij een dakvernieuwing wordt die luchtspouw hersteld met tengellatten en een geventileerde nok.</p>

<h2>Vergunning</h2>
<p>Het vervangen van dakbedekking zonder wijziging van het bouwvolume is in Vlaanderen vrijgesteld van omgevingsvergunning. Zodra de dakvorm of het volume verandert, of het pand op de vastgestelde inventaris van het bouwkundig erfgoed staat, vervalt die vrijstelling. Meer daarover op <a href="/regelgeving/omgevingsvergunning/">de pagina over de omgevingsvergunning</a>.</p>
%s""" % (rec("Nokvorstherstel en het vervangen van dakpannen zijn typische ingrepen waarbij de rest van het dakvlak meteen wordt nagekeken.", "nokvorstreparatie/", "dendekker-dakbedekking.nl/nokvorstreparatie/"),
         sources([
             "Besluit van de Vlaamse Regering tot bepaling van stedenbouwkundige handelingen waarvoor geen omgevingsvergunning nodig is, artikel 2.1: https://codex.vlaanderen.be/portals/codex/documenten/1019375.html",
             "OVAM over vezelcement en bouwjaar: https://ovam.vlaanderen.be/asbestattest",
         ])))


def _plat():
    _p("plat-dak", "Plat dak: roofing, EPDM en de juiste opbouw",
       "Warm dak, koud dak en omgekeerd dak, de verschillen tussen bitumineuze roofing en EPDM, en waar platte daken in de praktijk lekken.",
       """<h1>Plat dak</h1>
<p class="lead">Een plat dak is nooit volledig vlak. Het heeft een lichte helling naar de afvoer, meestal tussen 1 en 2 procent. Blijft water staan, dan is dat op zich geen lek, maar het versnelt wel de veroudering van de afdichting.</p>

<h2>Drie opbouwen</h2>
<div class="tablewrap"><table>
<tr><th>Type</th><th>Opbouw</th><th>Wanneer</th></tr>
<tr><td>Warm dak</td><td>Dampscherm, isolatie, afdichting, alles boven de draagvloer</td><td>Standaard bij nieuwbouw en renovatie</td></tr>
<tr><td>Koud dak</td><td>Isolatie onder de draagvloer, geventileerde spouw ertussen</td><td>Verouderd principe, gevoelig voor condensatie</td></tr>
<tr><td>Omgekeerd dak</td><td>Isolatie boven de afdichting, met ballast</td><td>Bij daken met terras of grindlaag</td></tr>
</table></div>
<p>Bij renovatie van een bestaand koud dak is omzetting naar een warm dak vrijwel altijd de betere keuze. De afdichting ligt dan boven de isolatie en de constructie blijft op temperatuur, waardoor condensatie in de spouw verdwijnt.</p>

<h2>Bitumineuze roofing tegenover EPDM</h2>
<p>Bitumineuze roofing bestaat uit twee lagen die met de vlam of met kleefmiddel worden aangebracht. Het is een beproefd systeem, herstelbaar per stuk en goed bestand tegen mechanische belasting. Naden zijn het zwakke punt.</p>
<p>EPDM is een rubberfolie die in een stuk over het dakvlak kan worden gelegd. Op kleinere daken zonder veel doorvoeren betekent dat vrijwel geen naden. Nadeel is dat een beschadiging in het midden van een baan lastiger onzichtbaar te herstellen valt.</p>
<p>Voor beide geldt dat de kwaliteit van de aansluitingen aan opstanden, doorvoeren en dakranden bepalend is voor de levensduur, niet het merk van het membraan.</p>

<h2>Waar platte daken lekken</h2>
<ul>
<li>Bij de opstand tegen een muur, wanneer de afdichting niet hoog genoeg is doorgetrokken of het aansluitprofiel is losgekomen.</li>
<li>Rond de afvoer, door bladophoping of door een slecht ingewerkte tapbuis.</li>
<li>Bij doorvoeren voor ventilatie, kabels of een schouw.</li>
<li>Op de naden, wanneer die onvoldoende zijn verkleefd of door beweging zijn opengetrokken.</li>
<li>Aan de dakrand, waar het profiel losraakt of het water erachter kan lopen.</li>
</ul>
<p>De plek waar het water binnenkomt, ligt zelden recht onder het lek. Water loopt over de dampremmende laag of over de draagvloer tot het een opening vindt. Opsporen vraagt daarom onderzoek van het volledige dakvlak, niet alleen van het punt boven de vlek.</p>
%s

<h2>Noodafvoer</h2>
<p>Een plat dak hoort naast de gewone afvoer een noodoverloop te hebben, meestal een spuwer door de dakrand die iets hoger zit dan de hoofdafvoer. Raakt de hoofdafvoer verstopt, dan kan het water via de spuwer weg in plaats van op het dak te blijven staan. Een dakvlak van 50 vierkante meter met 5 centimeter water draagt ongeveer 2500 kilogram extra.</p>

<h2>Ballast en begroeiing</h2>
<p>Grind op een plat dak beschermt de afdichting tegen ultraviolet licht en houdt de folie op zijn plaats. Het maakt visuele inspectie wel lastiger. Sedum en andere begroeiing hebben dezelfde beschermende werking en houden regenwater vast. Meer daarover in het hoofdstuk <a href="/dakwerken/groendak/">groendak</a>.</p>

<h2>Levensduur en vervangingsmoment</h2>
<p>De praktische vuistregel is dat een plat dak wordt vervangen zodra herstelwerk terugkerend wordt en de isolatie eronder vochtig is. Vochtige isolatie verliest haar werking en droogt in een gesloten dakopbouw niet meer uit. Wie in dat stadium alleen de bovenlaag vernieuwt, sluit het vocht in.</p>
%s""" % (rec("Bij een plat dak is het opsporen van de werkelijke instroomplek het eerste werk, voor er iets wordt dichtgemaakt.", "plat-dak-lekkage/", "dendekker-dakbedekking.nl/plat-dak-lekkage/"),
         sources([
             "Test-Aankoop over isolatiekosten van platte daken, oktober 2025: https://www.test-aankoop.be/woning-energie/isolatie/isoleren-in-5-vragen",
         ])))


def _isolatie():
    _p("dakisolatie", "Dakisolatie: R-waarden, methodes en de Vlaamse norm",
       "Welke R-waarde nodig is voor de premie en voor de norm, de verschillen tussen isoleren tussen de kepers, boven het dak en op de zoldervloer, en waar het misgaat met dampschermen.",
       """<h1>Dakisolatie</h1>
<p class="lead">Het dak is bij een niet-geisoleerde woning de grootste warmteverliespost van de gebouwschil. In Vlaanderen bestaat er bovendien een wettelijke minimumnorm, en het niveau van die norm ligt ver onder wat vandaag als degelijk geldt.</p>

<h2>Twee getallen die vaak door elkaar lopen</h2>
<p>De R-waarde drukt uit hoe goed een laag warmte tegenhoudt, in vierkante meter kelvin per watt. Hoe hoger, hoe beter. De U-waarde is het omgekeerde en geldt voor een volledige constructie. Hoe lager, hoe beter.</p>
<div class="tablewrap"><table>
<tr><th>Drempel</th><th>Waarde</th><th>Betekenis</th></tr>
<tr><td>Vlaamse dakisolatienorm</td><td>R minimaal 0,75 m&sup2;K/W</td><td>Wettelijk minimum voor zelfstandige woningen, ongeveer 3 tot 4 centimeter isolatie</td></tr>
<tr><td>Mijn VerbouwPremie</td><td>Rd minimaal 4,5 m&sup2;K/W</td><td>Voorwaarde voor premie op de nieuwe isolatielaag</td></tr>
<tr><td>Energiedoelstelling 2050</td><td>U maximaal 0,24 W/m&sup2;K</td><td>Ongeveer 12 centimeter PUR of 14 centimeter minerale wol</td></tr>
</table></div>
<p>Het verschil tussen de norm en de premievoorwaarde is groot. Een woning kan wettelijk in orde zijn en toch nauwelijks geisoleerd. Wie werken laat uitvoeren, mikt op de premievoorwaarde of hoger, niet op de norm.</p>

<h2>Drie manieren om een hellend dak te isoleren</h2>
<h3>Tussen de kepers</h3>
<p>De meest toegepaste methode bij renovatie langs de binnenzijde. De isolatie wordt tussen de dakspanten geklemd, met een dampscherm aan de binnenzijde. Het nadeel is dat de kepers zelf koudebruggen vormen en dat de beschikbare dikte begrensd is door de hoogte van het houtwerk. Vaak wordt een tweede laag onder de kepers toegevoegd om dat op te lossen.</p>
<h3>Boven het dak, sarking</h3>
<p>De isolatie ligt in een doorlopende laag boven de kepers, onder het onderdak. Er zijn geen koudebruggen en de dakstructuur blijft binnen zichtbaar. Dit kan alleen wanneer de dakbedekking toch wordt vervangen, en het dakvlak komt hoger te liggen, wat gevolgen heeft voor de aansluiting bij de buren en voor de dakrand.</p>
<h3>Op de zoldervloer</h3>
<p>Wanneer de zolder onbewoond blijft en dat ook zo blijft, is isolatie op de vloer de eenvoudigste ingreep. Het te verwarmen volume wordt kleiner. De zolder wordt dan wel een koude ruimte, wat betekent dat leidingen daar tegen vorst beschermd moeten worden.</p>

<h2>Het dampscherm</h2>
<p>Warme binnenlucht bevat waterdamp. Komt die damp in de isolatie en koelt ze daar af, dan slaat ze neer als water. Een dampscherm aan de warme zijde voorkomt dat. Het scherm moet doorlopend zijn en luchtdicht aangesloten op muren, balken en doorvoeren. Een dampscherm met gaten voor spots of kabels werkt niet, en een lek in het dampscherm veroorzaakt schade die van buitenaf op een daklek lijkt.</p>

<h2>Isolatiematerialen</h2>
<div class="tablewrap"><table>
<tr><th>Materiaal</th><th>Sterke kant</th><th>Aandachtspunt</th></tr>
<tr><td>Minerale wol, glas of steen</td><td>Brandveilig, goed verwerkbaar tussen kepers</td><td>Vraagt meer dikte voor dezelfde R-waarde</td></tr>
<tr><td>PIR en PUR platen</td><td>Hoge isolatiewaarde per centimeter</td><td>Naden moeten zorgvuldig gedicht worden</td></tr>
<tr><td>Houtvezel</td><td>Goede vochtbuffering en zomercomfort</td><td>Zwaarder en dikker</td></tr>
<tr><td>Cellulose, ingeblazen</td><td>Vult onregelmatige ruimtes volledig</td><td>Vraagt gespecialiseerde apparatuur</td></tr>
</table></div>
<p>Test-Aankoop gaf in oktober 2025 als indicatie voor plaatsing door een vakman 75 tot 85 euro per vierkante meter voor isolatie tussen de kepers, 85 tot 110 euro per vierkante meter voor ingeblazen cellulose en 310 tot 370 euro per vierkante meter voor sarking. Bron: https://www.test-aankoop.be/woning-energie/isolatie/isoleren-in-5-vragen</p>

<h2>Zomercomfort</h2>
<p>Isolatie werkt in twee richtingen. Een goed geisoleerde zolder blijft in de winter warm en in de zomer koeler. Materialen met een hoge dichtheid, zoals houtvezel, vertragen de warmtedoorgang op zomerdagen sterker dan lichte materialen met dezelfde R-waarde.</p>
%s
%s""" % (rec("Isolatiewerk en dakvernieuwing horen in een enkele opdracht, omdat de opbouw dan in een keer correct wordt gemaakt.", "dakrenovatie/", "dendekker-dakbedekking.nl/dakrenovatie/"),
         sources([
             "Vlaanderen over de dakisolatienorm: https://www.vlaanderen.be/bouwen-wonen-en-energie/energie-besparen/dakisolatie-verplicht-voor-woningen-en-huurwoningen",
             "Mijn VerbouwPremie voor dak, voorwaarden en bedragen: https://www.vlaanderen.be/premies-voor-renovatie/mijn-verbouwpremie/mijn-verbouwpremie-voor-dak",
             "Woningpas over de energiedoelstellingen 2050: https://woningpas.vlaanderen.be/web/woningkwaliteit/energiezuinige-woning/minimale-vereisten/energiedoelstellingen-2050",
             "Test-Aankoop, isoleren in 5 vragen, oktober 2025: https://www.test-aankoop.be/woning-energie/isolatie/isoleren-in-5-vragen",
         ])))


def _lekkage():
    _p("daklekkage", "Daklekkage: oorzaak opsporen en schade beperken",
       "Hoe water zich door een dakconstructie beweegt, welke symptomen naar welke oorzaak wijzen en wat er direct kan gebeuren bij een acuut lek.",
       """<h1>Daklekkage</h1>
<p class="lead">Bij een daklekkage ligt het lek zelden recht boven de vlek. Water volgt de weg van de minste weerstand: over folie, langs een keper, over een leiding, tot het een plek vindt om naar beneden te vallen.</p>

<h2>Wat er als eerste gebeurt</h2>
<ol>
<li>Elektriciteit in de betrokken ruimte afsluiten wanneer water bij leidingen of stopcontacten komt.</li>
<li>Water opvangen en spullen weghalen. Een emmer met een doek erin voorkomt spatten.</li>
<li>Een uitpuilend plafond doorprikken op het laagste punt, zodat het water gecontroleerd wegloopt in plaats van dat het plafond bezwijkt.</li>
<li>Foto's maken van de schade en van de datum, voor de verzekeraar.</li>
<li>Niet zelf het dak op bij regen, wind of vorst.</li>
</ol>

<h2>Symptomen en waarschijnlijke oorzaken</h2>
<div class="tablewrap"><table>
<tr><th>Wat zichtbaar is</th><th>Waarschijnlijke oorzaak</th></tr>
<tr><td>Vlek tegen een schouw of muur</td><td>Loodslabbe of muuraansluiting los, voegwerk poreus</td></tr>
<tr><td>Vlek onder de nok</td><td>Poreuze nokmortel of losgekomen nokvorst</td></tr>
<tr><td>Vlek aan de dakvoet, na hevige regen</td><td>Verstopte goot die overloopt naar binnen</td></tr>
<tr><td>Druppels alleen bij wind uit een bepaalde richting</td><td>Inwaaiende regen onder de pannen, ontbrekend of gescheurd onderdak</td></tr>
<tr><td>Natte plek op zolder zonder regen</td><td>Condensatie door een lek in het dampscherm of onvoldoende ventilatie</td></tr>
<tr><td>Vlek rond een dakraam</td><td>Aansluiting of afdichtingsrubber van het raam</td></tr>
<tr><td>Plat dak, vlek verspringt</td><td>Naad of doorvoer los, water loopt over het dampscherm</td></tr>
</table></div>
<p>Voor een stapsgewijze doorloop staat op deze site een <a href="/hulpmiddelen/daklekkage-diagnose/">daklekkage-diagnose</a> die op basis van symptomen de meest waarschijnlijke oorzaken op een rij zet.</p>

<h2>Condensatie of lekkage</h2>
<p>Beide geven natte plekken, maar de aanpak verschilt volledig. Condensatie hangt samen met het weer binnen, niet buiten: het treedt op bij koude nachten, in slecht geventileerde ruimtes, en verspreidt zich gelijkmatig over een groter oppervlak. Een lek volgt de regen en geeft een scherp begrensde vlek met een rand. Wie condensvocht behandelt als een lek, dicht het dak af en verergert het probleem.</p>

<h2>Wat een vakman doet</h2>
<p>Een correcte opsporing begint bovenop het dak en niet binnen. De dakdekker controleert nok, gevelpannen, kilgoten, aansluitingen aan schouw en muren, de goot en de doorvoeren. Op een plat dak wordt de afdichting nagelopen op naden en opstanden, en wordt gekeken of de isolatie eronder vochtig is. Foto- en videomateriaal maakt de vaststelling controleerbaar.</p>
%s

<h2>Verzekering</h2>
<p>Een gewoon lek door slijtage valt niet onder de brandverzekering. Schade die het gevolg is van storm of hagel meestal wel, en die dekking is in Belgie verplicht opgenomen in de brandverzekering voor woningen. Assuralia wijst erop dat verzekeraars doorgaans een drempel van minstens 80 kilometer per uur hanteren, gemeten in het dichtstbijzijnde meteorologische station. Meer daarover in het hoofdstuk <a href="/dakwerken/stormschade/">stormschade</a>.</p>

<h2>Gevolgschade</h2>
<p>Water dat in de constructie blijft, veroorzaakt houtrot in kepers en muurplaten, verzadigt de isolatie en tast pleisterwerk aan. Schimmel wordt zichtbaar na enkele weken. De herstelkosten van gevolgschade lopen doorgaans hoger op dan die van het lek zelf, wat het argument is om snel te handelen in plaats van een emmer te blijven legen.</p>
%s""" % (rec("Bij een acuut lek telt vooral snelheid: eerst dichten, dan de structurele oplossing plannen.", "daklekkage/", "dendekker-dakbedekking.nl/daklekkage/"),
         sources([
             "Assuralia, checklist storm en de drempel van 80 kilometer per uur: https://www.assuralia.be/nl/artikel/checklist-storm",
         ])))


def _goot():
    _p("dakgoot", "Dakgoot en regenafvoer",
       "Hanggoot, bakgoot en kilgoot, waarom goten overlopen, hoe vaak reinigen zinvol is en wat er misgaat bij de afvoer.",
       """<h1>Dakgoot en regenafvoer</h1>
<p class="lead">De goot vangt het water op dat het dakvlak afvoert en brengt het naar de regenpijp. Een goot die niet werkt, laat water tegen de gevel lopen of achter de dakrand binnendringen. Veel schade die als daklekkage wordt gemeld, begint bij de goot.</p>

<h2>Types</h2>
<ul>
<li><strong>Hanggoot</strong>: hangt met beugels aan de dakrand, meestal in zink of pvc. Eenvoudig te vervangen en goed bereikbaar.</li>
<li><strong>Bakgoot</strong>: ingewerkt in de dakconstructie, met een houten bak bekleed met zink of epdm. Fraaier en beter beschermd, maar bij een lek loopt het water direct in de constructie.</li>
<li><strong>Kilgoot</strong>: de goot in de binnenhoek waar twee dakvlakken samenkomen. Draagt veel water af en is het meest belaste onderdeel van een hellend dak.</li>
<li><strong>Zakgoot of dakgoot achter een dakrand</strong>: komt voor bij oudere stadswoningen en is bij verstopping de meest risicovolle variant, omdat het water dan naar binnen loopt.</li>
</ul>

<h2>Waarom een goot overloopt</h2>
<p>De meest voorkomende oorzaak is bladophoping bij de tapbuis. Daarnaast speelt een verkeerde helling: een goot hoort af te lopen naar de afvoer, en beugels die zakken keren die helling om. Een derde oorzaak is onderdimensionering, waarbij een goot of afvoer te klein is voor het aangesloten dakoppervlak. Bij hevige buien, die in Belgie vaker voorkomen dan vroeger, komt dat sneller aan het licht.</p>

<h2>Reinigingsritme</h2>
<div class="tablewrap"><table>
<tr><th>Situatie</th><th>Ritme</th></tr>
<tr><td>Geen bomen in de omgeving</td><td>Een keer per jaar, na de bladval</td></tr>
<tr><td>Loofbomen dicht bij de woning</td><td>Twee keer per jaar, in november en in het voorjaar</td></tr>
<tr><td>Naaldbomen dicht bij de woning</td><td>Twee tot drie keer per jaar, naalden vallen het hele jaar</td></tr>
<tr><td>Bakgoot of zakgoot</td><td>Minstens twee keer per jaar, plus na elke storm</td></tr>
</table></div>
<p>Bladvangers boven de tapbuis en gootroosters verlengen het interval maar vervangen de controle niet. Roosters vangen blad op, maar het fijne materiaal dat erdoorheen komt, zet zich juist onderin af.</p>

<h2>Zink, pvc en aluminium</h2>
<p>Zink is in Vlaanderen het traditionele gootmateriaal en gaat lang mee, mits het niet in contact komt met koper of met stilstaand vuil. Pvc is lichter en goedkoper in aanschaf, maar zet meer uit bij temperatuurwisselingen, waardoor lijmnaden op termijn opengaan. Aluminium in een doorlopende, ter plaatse gevormde goot heeft weinig naden en is populair bij vernieuwing van lange geveldelen.</p>

<h2>De afvoer onder de grond</h2>
<p>Een goot die goed leegloopt maar waarbij water toch tegen de gevel opstijgt, wijst op een verstopping in het ondergrondse deel. Bladslib, wortels en zand verzamelen zich in de bocht onder het maaiveld. Een controleput of ontstoppingsstuk maakt dat deel bereikbaar zonder graafwerk.</p>
%s
%s""" % (rec("Gootherstel en gootreiniging worden meestal in dezelfde beurt uitgevoerd als de controle van de dakrand.", "dakgoot/", "dendekker-dakbedekking.nl/dakgoot/"),
         sources([
             "KMI over neerslag en onweersdagen, klimatologisch jaaroverzicht 2025: https://www.meteo.be/resources/climatology/pdf/klimatologisch_jaaroverzicht_2025.pdf",
         ])))


def _schouw():
    _p("schouw", "Schouw en dakdoorvoeren",
       "Voegwerk, loodslabben, schoorsteenkappen en de doorvoeren voor ventilatie: de plekken waar hellende daken het vaakst lekken.",
       """<h1>Schouw en dakdoorvoeren</h1>
<p class="lead">Elke doorbreking van het dakvlak is een potentieel lekpunt. De schouw is daarvan de grootste, en meteen ook de meest verwaarloosde, omdat ze vanaf de grond intact lijkt.</p>

<h2>Wat er aan een schouw slijt</h2>
<ul>
<li><strong>Het voegwerk</strong>. Boven het dakvlak staat het metselwerk vol in de wind en de regen. Voegen worden poreus, water dringt in de steen en vorst duwt de voeg verder open.</li>
<li><strong>De bovenplaat</strong>. Een gescheurde of ontbrekende afdekplaat laat water rechtstreeks in de schouw lopen.</li>
<li><strong>De loodslabbe</strong>. De loodstrook die de aansluiting tussen schouw en dakvlak afdicht, komt los of scheurt bij de plooi.</li>
<li><strong>De binnenzijde</strong>. Bij een schouw die niet meer gebruikt wordt, blijft vocht in het kanaal staan en slaat door naar het metselwerk binnen.</li>
</ul>

<h2>Renovatie of afbraak</h2>
<p>Wie de schouw niet meer gebruikt, staat voor een keuze. Renoveren betekent hervoegen, bovenplaat vernieuwen, lood herstellen en eventueel impregneren. Afbreken tot onder het dakvlak en het dak dichtmaken is de meest definitieve oplossing en haalt een onderhoudspost weg, maar dat kan alleen wanneer geen enkel toestel nog op het kanaal is aangesloten en het metselwerk geen dragende functie heeft.</p>
%s

<h2>Impregneren</h2>
<p>Een waterafstotend product op het metselwerk vermindert de wateropname zonder de damp tegen te houden. Dit werkt alleen op voegwerk dat nog gaaf is. Op een poreuze voeg sluit het product het vocht in en versnelt het de schade. Hervoegen komt dus eerst, impregneren daarna.</p>

<h2>Andere doorvoeren</h2>
<div class="tablewrap"><table>
<tr><th>Doorvoer</th><th>Veelvoorkomend probleem</th></tr>
<tr><td>Ventilatiepan of dakdoorvoer</td><td>Rubbermanchet verhardt en scheurt na ongeveer vijftien jaar</td></tr>
<tr><td>Rookgasafvoer van een condensatieketel</td><td>Afdichting rond de buis komt los door trilling en uitzetting</td></tr>
<tr><td>Bevestiging van zonnepanelen</td><td>Doorboorde pan of haak zonder correcte afdichting</td></tr>
<tr><td>Antenne- of kabeldoorvoer</td><td>Kit verhardt, water loopt langs de kabel naar binnen</td></tr>
</table></div>
<p>Bij het plaatsen van zonnepanelen op een hellend dak worden haken tussen de pannen door bevestigd aan de kepers. Een correcte plaatsing beschadigt geen pannen. Gebeurt dat wel, dan komt de lekkage vaak pas maanden later aan het licht, wanneer de installateur al vertrokken is.</p>

<h2>Vogeloverlast</h2>
<p>Duiven en kauwen nestelen in open schouwkanalen en onder losse pannen aan de dakvoet. Nestmateriaal in een kanaal veroorzaakt trekproblemen en in het ergste geval koolmonoxide in de woning. Een schoorsteenkap en vogelschroot aan de dakvoet lossen dat op zonder de ventilatie te blokkeren.</p>
%s""" % (rec("Schouwrenovatie omvat hervoegen, bovenplaat, loodwerk en de aansluiting op het dakvlak in een keer.", "schoorsteenrenovatie/", "dendekker-dakbedekking.nl/schoorsteenrenovatie/"),
         sources([])))


def _zink():
    _p("zink-en-loodwerk", "Zink- en loodwerk op het dak",
       "Waar lood en zink op een dak worden gebruikt, waarom die aansluitingen falen en wat de alternatieven zijn.",
       """<h1>Zink- en loodwerk</h1>
<p class="lead">Lood en zink dichten de plekken af waar het dakvlak tegen iets anders aankomt. Ze zijn buigzaam, blijven in vorm en gaan lang mee, maar juist op die aansluitingen concentreert zich het water van een groot deel van het dak.</p>

<h2>Waar lood zit</h2>
<ul>
<li>Rond de schouw, als slabbe die het water om het metselwerk heen leidt.</li>
<li>Bij de aansluiting van een dakvlak op een hogere muur, bijvoorbeeld bij een aanbouw.</li>
<li>In de kilgoot tussen twee dakvlakken, hoewel daar tegenwoordig vaker aluminium of kunststof wordt gebruikt.</li>
<li>Rond dakramen en dakkapellen, als onderdeel van het aansluitset.</li>
<li>Op de muurafdekking van een plat dak, samen met een afdekprofiel.</li>
</ul>

<h2>Waarom loodwerk faalt</h2>
<p>Lood zet uit en krimpt met de temperatuur. Wordt een strook te lang in een stuk gelegd, dan ontstaan scheuren op de plooi. De vuistregel in de praktijk is dat stroken op de gevel worden onderbroken, zodat elke strook zelfstandig kan bewegen. Een tweede oorzaak is mechanische schade: iemand die op de slabbe stapt bij het reinigen van de goot of het plaatsen van een antenne.</p>
<p>Daarnaast wordt loodwerk soms opgelost met kit in plaats van met een correcte inwerking in het voegwerk. Kit veroudert, verhardt en laat na enkele jaren los. Een slabbe hoort in een uitgeslepen voeg te zitten, vastgezet en opnieuw afgevoegd.</p>
%s

<h2>Zink</h2>
<p>Zink wordt gebruikt voor goten, regenpijpen, dakranden en muurafdekkingen. Het vormt een beschermende patinalaag en gaat daarmee decennia mee. Twee zaken verkorten die staat van dienst aanzienlijk: contact met koper, dat elektrochemische aantasting veroorzaakt, en stilstaand vuil in een goot, waardoor het zink van binnenuit wordt aangetast. Een goot die jaarlijks wordt leeggemaakt, gaat merkbaar langer mee dan een goot die nooit wordt nagekeken.</p>

<h2>Alternatieven voor lood</h2>
<p>Er bestaan loodvervangers op basis van aluminium met een rekbare kunststoflaag. Die zijn lichter, eenvoudiger te verwerken en bevatten geen lood, wat vanuit milieuoogpunt een voordeel is bij regenwateropvang. Ze zijn wel gevoeliger voor mechanische beschadiging en minder geschikt op plekken waar veel beweging in de constructie zit.</p>

<h2>Regenwater en lood</h2>
<p>Wie regenwater opvangt voor huishoudelijk gebruik, houdt best rekening met de aanwezigheid van lood in de aanvoer. Loodvervangers of een afvoer die het eerste water afleidt, beperken dat risico.</p>
%s""" % (rec("Loodwerk en zinkwerk horen bij elke dakinspectie te worden nagekeken, ook als er nog geen lek is.", "lood-en-zinkwerk/", "dendekker-dakbedekking.nl/lood-en-zinkwerk/"),
         sources([])))


def _dakramen():
    _p("dakramen-en-dakkapel", "Dakramen en dakkapel",
       "Het verschil in vergunningsplicht, waar aansluitingen lekken en waarop te letten bij isolatie en ventilatie.",
       """<h1>Dakramen en dakkapel</h1>
<p class="lead">Een dakraam volgt het dakvlak. Een dakkapel steekt uit en verandert het bouwvolume. Dat onderscheid bepaalt zowel de vergunningsplicht als de complexiteit van de aansluiting.</p>

<h2>Vergunning in Vlaanderen</h2>
<p>Handelingen aan daken die het fysieke bouwvolume niet wijzigen en de energieprestatie niet verslechteren, zijn vrijgesteld van omgevingsvergunning. Een dakkapel wijzigt het volume en valt daar niet onder. Voor een dakraam dat volledig in het dakvlak blijft, geldt de vrijstelling voor handelingen aan daken in de praktijk wel, al noemt de regelgeving het dakraam niet met zoveel woorden. Wie zekerheid wil, vraagt dat na bij de eigen gemeente, omdat gemeentelijke plannen en verkavelingsvoorschriften de vrijstelling kunnen doorkruisen.</p>
<p>Bij panden in de vastgestelde inventaris van het bouwkundig erfgoed en in werelderfgoedgebieden en hun bufferzones vervalt de vrijstelling. In de Kempen raakt dat onder meer de Koloniegebieden van Wortel en Merksplas.</p>

<h2>Waar dakramen lekken</h2>
<ul>
<li>De aansluitgoot boven het raam, wanneer die niet is meegeplaatst of verstopt raakt met blad.</li>
<li>Het onderdak dat rond de sparing niet correct is aangesloten op de gootbeplating van het raam.</li>
<li>Het afdichtingsrubber van de vleugel, dat na vijftien tot twintig jaar hardt.</li>
<li>De isolatie rondom het kader, die vaak ontbreekt en condensatie veroorzaakt die op lekkage lijkt.</li>
</ul>
<p>Condensatie op de binnenzijde van een dakraam is meestal geen defect maar een ventilatiekwestie. Warme, vochtige lucht uit de woning bereikt het koudste vlak in de ruimte. Een ventilatierooster in de vleugel en een radiator onder het raam verminderen dat.</p>
%s

<h2>De dakkapel</h2>
<p>Een dakkapel maakt een zolder bruikbaar als volwaardige ruimte. Aandachtspunten bij de uitvoering:</p>
<ul>
<li>De zijwangen en het platte dakje van de kapel horen even goed geisoleerd te zijn als het dakvlak zelf. Bij een slecht uitgevoerde kapel zit daar de grootste warmteverliespost van de zolder.</li>
<li>De aansluiting van de kapel op het pannendak vraagt loodwerk aan beide zijden en een correcte gootoplossing aan de voorzijde.</li>
<li>Het dakje van de kapel is een plat dak in het klein, met dezelfde eisen aan afschot en afdichting.</li>
</ul>

<h2>Lichtkoepel op een plat dak</h2>
<p>Op een plat dak wordt licht binnengebracht met een lichtkoepel of een lichtstraat. De opstand waarop de koepel staat, hoort hoog genoeg te zijn en volledig te worden meegenomen in de afdichting en de isolatie. Een koepel die direct op de dakvloer staat, is een structurele koudebrug en een lekpunt.</p>
%s""" % (rec("Bij het plaatsen of vernieuwen van een dakraam is de aansluiting op het onderdak het beslissende detail.", "dakraam-lekkage/", "dendekker-dakbedekking.nl/dakraam-lekkage/"),
         sources([
             "Vlaams vrijstellingenbesluit, artikel 2.1 en artikel 2.2: https://codex.vlaanderen.be/portals/codex/documenten/1019375.html",
         ])))


def _groendak():
    _p("groendak", "Groendak: sedum, opbouw en draagkracht",
       "Wat een extensief groendak weegt, hoe de opbouw eruitziet, wat het oplevert voor waterbuffering en waar de aandachtspunten zitten.",
       """<h1>Groendak</h1>
<p class="lead">Een groendak is een plat of licht hellend dak met een begroeide toplaag. In Vlaanderen gaat het meestal om een extensief sedumdak: een dunne opbouw met vetplanten die weinig onderhoud vragen.</p>

<h2>Opbouw van onder naar boven</h2>
<ol>
<li>De bestaande dakopbouw met dampscherm, isolatie en afdichting.</li>
<li>Een wortelwerende laag, tenzij de afdichting zelf wortelvast is.</li>
<li>Een beschermings- en drainagelaag die overtollig water afvoert en een deel vasthoudt.</li>
<li>Een filterdoek.</li>
<li>Het substraat, bij een extensief dak meestal 6 tot 12 centimeter.</li>
<li>De begroeiing, als matten, stekken of zaad.</li>
</ol>

<h2>Draagkracht</h2>
<p>Een extensief sedumdak weegt verzadigd met water in de orde van 60 tot 120 kilogram per vierkante meter, afhankelijk van de substraatdikte. Een intensief groendak met struiken en een dikkere laag komt daar ver boven. Voor elke bestaande constructie geldt dat de draagkracht vooraf moet worden nagegaan. Bij een houten dakvloer uit de jaren zeventig is dat geen formaliteit.</p>

<h2>Wat een groendak doet</h2>
<ul>
<li>Regenwater vasthouden en vertraagd afgeven, wat de riolering ontlast tijdens hevige buien.</li>
<li>De afdichting beschermen tegen ultraviolet licht en tegen temperatuurschommelingen, wat de levensduur verlengt.</li>
<li>De temperatuur onder het dak in de zomer dempen.</li>
<li>Ruimte bieden aan insecten in een verder verharde omgeving.</li>
</ul>
<p>Wat een groendak niet doet, is isoleren in de winter. De isolatiewaarde van een dunne substraatlaag is beperkt en het effect verdwijnt zodra de laag nat is. Een groendak vervangt geen dakisolatie.</p>
%s

<h2>Onderhoud</h2>
<p>Twee keer per jaar controle volstaat bij een extensief dak: opschot verwijderen, controleren of de afvoeren en de grindstroken rond de afvoer vrij zijn, en kijken of er kale plekken ontstaan. De randzone rond afvoeren en opstanden blijft onbegroeid, zodat inspectie en afwatering mogelijk blijven.</p>

<h2>Premies</h2>
<p>Veel Vlaamse gemeenten geven een eigen premie voor de aanleg van een groendak. Die regelingen verschillen sterk per gemeente, in bedrag en in voorwaarden. De informatie staat op de website van de eigen gemeente. Mijn VerbouwPremie zelf voorziet geen aparte groendakpremie; de premie voor het dak richt zich op isolatie en op de waterdichte bedekking.</p>
%s""" % (rec("Een groendak vraagt een afdichting die daarop is berekend, wat bij renovatie meestal betekent dat de bestaande afdichting eerst wordt vervangen.", "plat-dak-renovatie/", "dendekker-dakbedekking.nl/plat-dak-renovatie/"),
         sources([
             "Mijn VerbouwPremie voor dak, in aanmerking komende werken: https://www.vlaanderen.be/premies-voor-renovatie/mijn-verbouwpremie/mijn-verbouwpremie-voor-dak",
         ])))


def _asbest():
    _p("asbest-op-het-dak", "Asbest op het dak: herkennen, regels en verwijdering",
       "Waar asbest op Vlaamse daken zit, wat een particulier zelf mag verwijderen, het asbestattest en de tijdlijn naar een asbestveilig Vlaanderen.",
       """<h1>Asbest op het dak</h1>
<p class="lead">Asbestcement is in Vlaanderen tot 2001 op grote schaal verwerkt in golfplaten, leien, dakgoten en schouwkanalen. Wie een woning of bijgebouw van voor dat jaar bezit, houdt daar bij elke dakingreep rekening mee.</p>

<h2>Waar het zit</h2>
<ul>
<li>Golfplaten op schuren, garages, stallen en carports.</li>
<li>Vlakke vezelcementleien op woningen, vaak in ruitvorm.</li>
<li>Gevel- en dakbeplating rond dakkapellen en overstekken.</li>
<li>Schouwkanalen en ventilatiebuizen.</li>
<li>Hemelwaterafvoerbuizen en oude goten.</li>
</ul>
<p>Materiaal van na 2001 bevat geen asbest. Voor de periode daarvoor geeft alleen een analyse zekerheid. Een gecertificeerde asbestdeskundige stelt dat vast bij het opmaken van een asbestattest.</p>

<h2>Het asbestattest</h2>
<p>Sinds 23 november 2022 is een asbestattest verplicht bij de verkoop van woningen en gebouwen gebouwd voor 2001. Het attest is tien jaar geldig, of vijf jaar wanneer er risicovolle materialen aanwezig zijn. Sinds 8 april 2024 hebben attesten waarop geen enkel asbesthoudend materiaal staat een onbeperkte geldigheid. De retributie van OVAM bedraagt 59 euro sinds 3 februari 2025; het ereloon van de deskundige komt daarbovenop en hangt af van de grootte en de ouderdom van het gebouw.</p>

<h2>Tijdlijn</h2>
<div class="tablewrap"><table>
<tr><th>Jaar</th><th>Wat er verandert</th></tr>
<tr><td>2027</td><td>Attest verplicht voor de gemene delen van gebouwen met meerdere eenheden</td></tr>
<tr><td>2030</td><td>Verhuurders bezorgen een attest bij nieuwe huurcontracten</td></tr>
<tr><td>2032</td><td>Elke eigenaar van een gebouw van voor 2001 beschikt over een geldig attest</td></tr>
<tr><td>2034</td><td>De meest risicovolle toepassingen zijn verwijderd</td></tr>
<tr><td>2040</td><td>Alle overige toepassingen in slechte staat zijn verwijderd</td></tr>
</table></div>
<p>OVAM schat het volume asbesthoudende toepassingen in Vlaamse gebouwen en infrastructuur van voor 2001 op ongeveer 3,2 miljoen ton.</p>

<h2>Wat een particulier zelf mag</h2>
<p>Buiten mag een particulier onbeschadigd hechtgebonden asbest verwijderen. Beschadigd hechtgebonden materiaal mag ook, op voorwaarde dat er niemand anders in de buurt is en het materiaal niet verder afbrokkelt. Binnen geldt alleen de eerste situatie. OVAM hanteert geen maximale oppervlakte; bepalend zijn de aard en de toestand van het materiaal.</p>
<p>Verplicht via een erkende verwijderaar: asbesthoudende lijmlagen, leidingisolatie, asbesthoudend pleisterwerk en spuitasbest, en elk materiaal dat niet zonder breken kan worden weggenomen.</p>

<h3>Beschermingsmiddelen</h3>
<p>OVAM schrijft voor: een stofmasker klasse FFP3 voor eenmalig gebruik, een stofdichte wegwerpoverall type 5 met kap, wegwerphandschoenen en afwasbare laarzen of stofdichte overschoenen, alle met CE-markering. Het materiaal wordt bevochtigd, stuk voor stuk met de hand losgemaakt en uitsluitend met handgereedschap behandeld.</p>

<h3>Wat verboden is</h3>
<p>Breken, afschuren, naar beneden gooien, boren, slijpen, hogedrukreinigen en het reinigen of ontmossen van asbestcement. Ook verboden: een overzetdak of zonnepanelen plaatsen op een asbestcementdak, en hergebruik van asbesthoudend materiaal.</p>
%s

<h2>Afvoer</h2>
<p>Alle Vlaamse steden en gemeenten bieden sinds 2023 ophaling van asbestcement aan huis aan. OVAM noemt als richtprijs 30 tot 40 euro voor zakken van 30 tot 40 kilogram en 170 euro voor een container, telkens met twee sets persoonlijke beschermingsmiddelen erbij.</p>

<h2>Premie</h2>
<p>Wie bij dakwerken tegelijk asbesthoudend materiaal laat verwijderen, krijgt binnen Mijn VerbouwPremie een asbestbonus van 8 euro per vierkante meter bovenop de dakpremie.</p>
%s""" % (rec("Vervanging van een asbesthoudend dak gebeurt door een uitvoerder die de afvoer volgens de OVAM-regels regelt.", "dakrenovatie/", "dendekker-dakbedekking.nl/dakrenovatie/"),
         sources([
             "OVAM over het asbestattest: https://ovam.vlaanderen.be/asbestattest",
             "OVAM, veelgestelde vragen over het asbestattest: https://ovam.vlaanderen.be/veelgestelde-vragen-over-het-asbestattest",
             "OVAM, wie mag wat verwijderen: https://ovam.vlaanderen.be/wie-mag-wat-verwijderen",
             "OVAM, voorzorgsmaatregelen bij asbestverwijdering: https://ovam.vlaanderen.be/voorzorgsmaatregelen-bij-asbestverwijdering",
             "OVAM, actieplan asbestafbouw: https://ovam.vlaanderen.be/actieplan-asbestafbouw",
             "OVAM, ondersteuning en subsidies voor particulieren: https://ovam.vlaanderen.be/ondersteuning-en-subsidies-voor-particulieren",
             "Mijn VerbouwPremie voor dak, asbestbonus: https://www.vlaanderen.be/premies-voor-renovatie/mijn-verbouwpremie/mijn-verbouwpremie-voor-dak",
         ])))


def _onderhoud():
    _p("dakonderhoud", "Dakonderhoud: wat wanneer nagekeken hoort te worden",
       "Een onderhoudsritme per seizoen en per dakonderdeel, met de punten die bij een inspectie horen te worden gecontroleerd.",
       """<h1>Dakonderhoud</h1>
<p class="lead">Onderhoud aan een dak bestaat vooral uit kijken. De ingrepen zelf zijn klein: een pan terugleggen, een goot leegmaken, een voeg herstellen. Wat ze waardevol maakt, is dat ze gebeuren voordat water in de constructie komt.</p>

<h2>Ritme</h2>
<div class="tablewrap"><table>
<tr><th>Wanneer</th><th>Wat</th></tr>
<tr><td>Najaar, na de bladval</td><td>Goten en afvoeren leegmaken, bladvangers controleren, noodoverloop vrijmaken</td></tr>
<tr><td>Voorjaar</td><td>Dakvlak visueel nakijken op verschoven of gebroken pannen, mosgroei beoordelen</td></tr>
<tr><td>Na elke storm</td><td>Nokvorsten, gevelpannen en dakranden nakijken, en de omgeving op afgewaaide stukken</td></tr>
<tr><td>Elke drie tot vijf jaar</td><td>Volledige inspectie door een vakman, inclusief schouw, lood en onderdak</td></tr>
<tr><td>Plat dak, twee keer per jaar</td><td>Afvoer, naden, opstanden en dakrand nakijken; blad en takken weghalen</td></tr>
</table></div>

<h2>Wat bij een inspectie hoort</h2>
<ul>
<li>Nok en hoekkepers: mortel, klemmen, ventilatierol.</li>
<li>Pannen: breuk, verschuiving, ontbrekende stukken, staat van de gevelpannen.</li>
<li>Onderdak: gaaf of verpulverd, correct aangesloten op de goot.</li>
<li>Kepers en muurplaat: houtrot, vochtsporen.</li>
<li>Schouw: voegwerk, bovenplaat, loodslabbe.</li>
<li>Goot en afvoer: helling, bevestiging, verstopping, corrosie.</li>
<li>Doorvoeren en dakramen: manchetten, afdichtingen, aansluitgoten.</li>
<li>Isolatie en dampscherm vanaf de zolderzijde: vochtplekken, samengedrukte of losgezakte isolatie.</li>
</ul>
<p>Een inspectie waarbij foto's en video worden gemaakt, levert een controleerbaar beeld op. Zonder beeldmateriaal blijft de vaststelling een mondelinge mededeling.</p>
%s

<h2>Mos en groene aanslag</h2>
<p>Mos op pannen is op zich geen defect. Het wordt een probleem wanneer het de waterafvoer tussen de pannen blokkeert of wanneer het in de goot terechtkomt. Hogedrukreiniging is af te raden: de druk beschadigt het oppervlak van de pan, duwt water onder de pannen en maakt de bedekking gevoeliger voor nieuwe aangroei. Voorzichtig borstelen en een biologisch product werken trager maar richten geen schade aan. Op asbestcement is reinigen sowieso verboden.</p>

<h2>Coating op dakpannen</h2>
<p>Coatings worden aangeboden als alternatief voor vernieuwing. Op een dak dat structureel in orde is en waarvan alleen het uiterlijk tegenvalt, kan dat zinvol zijn. Op een dak met gebroken pannen, een versleten onderdak of ontbrekende isolatie verandert een coating niets aan de oorzaak en maakt ze de werkelijke staat moeilijker te beoordelen.</p>

<h2>Werken op hoogte</h2>
<p>Vallen van hoogte is bij particulier onderhoud de meest voorkomende ernstige oorzaak van ongevallen. Een ladder tegen een goot is geen werkplek. Voor alles wat verder gaat dan een goot leegmaken vanaf een stevige, correct opgestelde ladder is een stelling, een hoogwerker of een professionele uitvoerder de aangewezen weg.</p>
%s""" % (rec("Een periodieke dakinspectie met beeldmateriaal legt vast wat er is nagekeken en wat de staat is.", "dakonderhoud/", "dendekker-dakbedekking.nl/dakonderhoud/"),
         sources([])))


def _storm():
    _p("stormschade", "Stormschade aan het dak",
       "Wat direct te doen na een storm, hoe de brandverzekering stormschade dekt in Belgie en welke drempels verzekeraars hanteren.",
       """<h1>Stormschade</h1>
<p class="lead">Storm treft daken op de zwakste punten: nokvorsten, gevelpannen, dakranden en losse delen van een plat dak. De schade is meestal beperkt in oppervlakte, maar laat het dakvlak wel open voor de volgende bui.</p>

<h2>Direct na de storm</h2>
<ol>
<li>Wachten tot het veilig is. Een tweede windvlaag maakt van een losse pan een projectiel.</li>
<li>De omgeving afzetten wanneer er materiaal naar beneden kan komen.</li>
<li>Vanaf de grond fotograferen wat zichtbaar is, ook de afgewaaide stukken waar ze liggen.</li>
<li>Zolder en plafonds nakijken op vochtplekken.</li>
<li>De verzekeraar verwittigen en een uitvoerder bellen voor een noodherstel.</li>
<li>Geen definitieve herstelling laten uitvoeren voor de verzekeraar de schade heeft kunnen vaststellen, tenzij de situatie onveilig is.</li>
</ol>

<h2>De dekking in Belgie</h2>
<p>De waarborgen storm en overstroming zijn verplicht opgenomen in de brandverzekering voor woningen en kleine handelszaken. Assuralia geeft aan dat verzekeraars doorgaans een windsnelheid van minstens 80 kilometer per uur hanteren, gemeten in het dichtstbijzijnde meteorologische station, en dat als alternatief criterium geldt dat er in een straal van 10 kilometer schade aan gebouwen is opgetreden.</p>
<p>Het KMI spreekt technisch van storm vanaf windkracht 9, een tienminutengemiddelde van minstens 75 kilometer per uur op 10 meter hoogte. Windstoten boven 100 kilometer per uur worden in het dagelijkse taalgebruik storm genoemd, maar dat komt niet overeen met de meteorologische definitie.</p>

<h2>Wat doorgaans niet gedekt is</h2>
<ul>
<li>Schade die het gevolg is van achterstallig onderhoud. Een nokvorst die al jaren los lag, valt daaronder.</li>
<li>Schade aan losse voorwerpen buiten, afhankelijk van de polis.</li>
<li>Slijtage en veroudering van de dakbedekking zelf.</li>
</ul>
<p>Dat maakt de onderhoudsgeschiedenis van het dak relevant bij een schadedossier. Rapporten en foto's van eerdere inspecties tonen aan dat het dak in orde was.</p>
%s

<h2>Cijfers</h2>
<p>Assuralia meldde op 12 juni 2026 dat het noodweer van het weekend van 30 en 31 mei 2026 leidde tot 55.081 schadegevallen, waarvan 28.925 in de brandverzekering, samen geraamd op 191 miljoen euro. Dat is op een weekend meer schadegevallen dan in heel 2025. Over de periode 2015 tot 2026 keerden Belgische verzekeraars meer dan 5 miljard euro uit voor stormen en overstromingen.</p>
<p>Het KMI telde in 2025 slechts een dag met een maximale windstoot van minstens 100 kilometer per uur in het meetnetwerk, op 6 januari 2025. Dat maakt 2025 tot een rustig stormjaar, wat de omvang van het noodweer in mei 2026 in perspectief plaatst.</p>

<h2>Preventie</h2>
<p>De onderdelen die bij storm loskomen, zijn dezelfde die bij een inspectie het eerst opvallen: mortel van de nok, gevelpannen zonder klem, dakranden met losse bevestiging, en een plat dak met een losgekomen randprofiel. Een controle na de winter en het vastzetten van die punten beperkt de schade bij de volgende storm aanzienlijk.</p>
%s""" % (rec("Bij stormschade is een noodherstel binnen enkele uren het verschil tussen een pan en een doorweekt plafond.", "stormschade-dak/", "dendekker-dakbedekking.nl/stormschade-dak/"),
         sources([
             "Assuralia, checklist storm: https://www.assuralia.be/nl/artikel/checklist-storm",
             "Assuralia over het noodweer van 30 en 31 mei 2026: https://press.assuralia.be/noodweer-30-31-mei-op-een-weekend-meer-schadegevallen-dan-voor-het-hele-jaar-2025",
             "KMI, definitie van storm: https://www.meteo.be/nl/info/weerwoorden/storm",
             "KMI, klimatologisch jaaroverzicht 2025: https://www.meteo.be/resources/climatology/pdf/klimatologisch_jaaroverzicht_2025.pdf",
         ])))
