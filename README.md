# Project 2

<H1> HTML </ h1>

<H2> layout.html </ h2>
<P>
layout.html se ne koristi extensivley zbog uobičajene namjene - kako bi omogućio nasljeđivanje mnogih sličnih html stranica. U ovoj aplikaciji za jednu stranicu,
samo index.html nasljeđuje od layout.html. Ipak, koristan je za iskorištavanje svih okvira i knjižnica koje koristim
kao što su Bootstrap 4, GoogleFonts, Ajax, Handlebars i moje vlastite prilagođene CSS i JS datoteke. Zato što nisam koristio previše ručki
JS Clientside predloške, samo sam uključio one koje sam koristio izravno u svom layout.html umjesto da ih faktoring out.
</ P>

<H2> Pocetna </ h2>
<P>
index.html nasljeđuje od layout.html i određuje položaj dvaju glavnih područja stranice - prikaz popisa kanala i
u prikazu poruke. Koristim jedan redak bootstrap 4, s 2 stupca, gdje je lijevi stupac prikaz popisa kanala, i
desni stupac je prikaz poruke. Primjenjujem kombinacije prilagođenih css i bootstrap 4 klase kako bih dobio izgled koji želim.
U suštini sam ga oblikovao tako da svaki stupac zauzima 100% stranice, a veličina stupca prikaza kanala ostaje konstantna, dok
stupac pregleda poruke dinamički mijenja veličinu kako se preglednik mijenja horizontalno.
</ P>

<h1> CSS i SCSS </h1>
<h2> styles.css & styles.scss </h2>
<p> Slično mojim drugim projektima, te datoteke sadrže stil koji koristim na mojoj web lokaciji. </p>

<h1> Javascript: klijent </h1>
<H2> index.js </ h2>
<p> index.js sadrži sav kôd na strani klijenta za aplikaciju za jednu stranicu. To je asinkroni kôd temeljen na događaju.
Različiti događaji koji pokreću JS kod za izvršenje uključuju učitavanje stranice putem GET zahtjeva, a korisnik klikne na kanal iz
popis kanala za prebacivanje kanala, a korisnik klikne na gumb za slanje kako bi poslao poruku u prikaz poruke. Osim događaja
koji su izravno rezultat djelovanja korisnika, drugi događaji su definirani kao primanje signala od Python poslužitelja
putem socketio. Postoje dvije ključne komponente koje čine aplikaciju dinamičnom - AJAX i Socketio. Uz AJAX, asinkroni POST zahtjevi
isporučivati ​​podatke o klijentu na poslužitelj. Na temelju podataka o klijentu, poslužitelj Python FLASK odgovara odgovarajućim JSON podacima.
Klijent koji je pokrenuo zahtjev primi JSON podatke, a JS kod u pregledniku analizira JSON na dinamički
dodajte prave podatke u desni prikaz. S Socketio, ja sam u mogućnosti provesti live poruka između korisnika. Kada klijent pošalje
najprije se preusmjerava na poslužitelj gdje je pohranjen za kasnije pronalaženje, a zatim se emitira svim korisnicima u kanalu
da je poslana putem funkcije emitiranja. Natrag na strani klijenta, socket.on () slušatelj sluša emitiranu poruku. Jer
JS kod u socket.on () slušatelju prima podatke putem emitiranja, kod izvršen u ovom bloku utječe na sve klijente u kanalu.
S obzirom na lokalno pohranjivanje, pohranjujem prikazno ime, trenutni kanal i podatke o dodatku po kanalu. Koriste se podaci za ispunu
za precizniji izgled prikaza komentara kao novog komentara.
</ P>

</ P>

<h1> Python: poslužitelj </h1>
<H2> application.py </ h2>
<p> application.py sadrži sav kôd na strani poslužitelja za moju aplikaciju za jednu stranicu. Ima jednu funkciju rute, indeks i
5 socketio slušatelja koji reagiraju na signale poslane putem emitiranog od JS klijenta. Također ima globalne varijable za pohranu podataka
trajnije. Prva globalna varijabla je rječnik u kojem je svaki ključ naziv kanala, a svaka vrijednost je popis
rječnici. Svaki rječnik u popisu rječnika može se smatrati komentarom, tako da unutar svakog rječnika komentara
su ključni parovi vrijednosti o sadržaju korisnika, vremenske oznake i poruke. Druga globalna varijabla je jednostavan rječnik
gdje je svaki ključ korisnik, a svaka vrijednost je kanal na kojem se nalaze. Indeks prve funkcije ponaša se različito ovisno
ako je GET ili POST zahtjev poslan. Ako je GET zahtjev poslan - događa se pri učitavanju prve stranice ili ako korisnik ručno osvježi
stranica - tada se stranica osvježava, a podaci o do sada stvorenim kanalima šalju se na stranicu. Ako je POST zahtjev bio
poslano - što se događa odmah nakon ručnog osvježavanja stranice, na prekidaču kanala ili na dodavanju kanala - POST dio funkcije
izvršava. Socketio slušatelji šalju poruku, pridružuju se, a na dopustu su odgovorni za rukovanje live poruka u određenom kanalu.
Funkcija slanja poruke dodaje novu poruku spremište na strani poslužitelja, briše posljednju poruku iz globalne pohrane ako postoje
više od 100 poruka, a zatim emitira poruku koju je primila svim klijentima iz kanala s kojeg je poslan.
Da bi znali koji su klijenti u kojim kanalima, koristim na dopustu i na pridruživanju, koji reagiraju na emitiranje signala sa strane klijenta
poslužitelja kada određeni klijent napušta sobu ili joj se pridružuje. Posljednji važan slušatelj socketio je odgovoran za rukovanje
"osobni dodir" ili dodatna značajka koju sam dodao aplikaciji. Pročitajte više o tome pod "Osobni dodir"
</ P>

<h1>Osobni osvrt  </h1>
<p> Za moj osobni osvrt, dodao sam prikazanom nazivu "superkorisnik" posebne povlastice. Točnije, dao sam im moć
da izbrišete bilo koji kanal i njegove komentare s poslužitelja i iz pogleda bilo kojeg drugog korisnika koji koristi aplikaciju. Za brisanje kanala,
ime za prikaz "superuser" mora biti u kanalu koji želi izbrisati i upisati "command delete {channel name here}".
Kada superkorisnik to učini, svi korisnici koji koriste aplikaciju dignu se s bilo kojeg kanala u kojem se nalaze i premještaju u opći, zajedno s
superkorisnik. Poruka se emitira na opće o tome koji je kanal superuser upravo izbrisao. Da biste spriječili slučajne korisnike iz
lako brišući kanale nevoljno, obmanjujem istinsko ime superkorisnika. Dakle, jedini način da osoba zna kako
da bi se dobila sposobnost superkorisnika da pogleda kod. Prosječan korisnik vjerojatno ga neće shvatiti ako im netko ne kaže.
Kada superkorisnik pošalje poruku, njegovo ime za prikaz se pojavljuje kao mod, ali kod klijentske strane koji daje superkorisniku ovu mogućnost provjerava
za korisničko ime "superuser". Ova značajka također je općenito korisna za "kontrolirano čišćenje" kanala s poslužitelja. Bez
značajka kao što je ovaj jedini način za čišćenje kanala bio bi ponovno pokretanje poslužitelja.
</ P>