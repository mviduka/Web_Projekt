# WEB_Projekt

<H1> HTML </ h1>

<H2> layout.html </ h2>
<P>
  U ovoj aplikaciji index.html nasljeđuje layout.html. Ipak, koristan je za iskorištavanje svih frameworka koje koristim
kao što su Bootstrap, GoogleFonts, Ajax, Handlebars, CSS i JS datoteke.
JS Clientside predloške, samo sam uključio one koje sam koristio izravno u layout.html.
</ P>

<H2> Pocetna </ h2>
<P>
index.html nasljeđuje od layout.html i određuje položaj dvaju glavnih područja stranice - prikaz popisa kanala i
u prikazu poruke.Primjenjujem kombinacije prilagođenih css i bootstrap klase kako bih dobio izgled koji želim.
Svaki stupac sam oblikova tako da zauzima 100% stranice,veličina stupca ostaje konstantna, dok
stupac pregleda poruke dinamički mijenja veličinu kako se preglednik mijenja horizontalno.
</ P>

<h1> CSS i SCSS </h1>
<h2> styles.css & styles.scss </h2>
<p> Te datoteke sadrže stil koji koristim na web projektu. </p>

<h1> Javascript: klijent </h1>
<H2> index.js </ h2>
<p> index.js sadrži sav kod na strani klijenta za aplikaciju za jednu stranicu.
Pokretanjem JS koda za izvršenje uključuju učitavanje stranice putem GET zahtjeva.Dvije ključne komponente koje čine aplikaciju dinamičnom - AJAX i Socketio. Na temelju podataka o klijentu, poslužitelj Python FLASK odgovara odgovarajućim JSON podacima.
Klijent koji je pokrenuo zahtjev primi JSON podatke.Sa Socketio je moguće slati poruke između korisnika. Kada klijent pošalje poruku
najprije se preusmjerava na server gdje se pohranjuje za kasniju pretragu, a zatim se šalje svim korisnicima u kanalu.
Socket.on () čita poslanu poruku.Kod izvršen u ovom bloku utječe na sve klijente u kanalu.
S obzirom na lokalno pohranjivanje, pohranjuje se ime, trenutni kanal i podatke o kanalu.
</ P>

</ P>

<h1> Python: poslužitelj </h1>
<H2> application.py </ h2>
<p> application.py ima jednu funkciju rute, indeks i 5 socketio koji reagiraju na signale poslane putem JS filea. Također ima globalne varijable za pohranu podataka trajnije. Prva globalna varijabla je rječnik u kojem je svaki ključ naziv kanala.Druga globalna varijabla je jednostavan rječnik
gdje je svaki ključ korisnik, a svaka vrijednost je kanal na kojem se nalaze. Indeks prve funkcije ponaša se različito ovisno
ako je GET ili POST zahtjev poslan. Ako je GET zahtjev poslan pri učitavanju prve stranice ili ako korisnik ručno osvježi
stranicu tada se stranica osvježava, a podaci o stvorenim kanalima šalju se na stranicu. Ako je POST zahtjev  POST dio funkcije se
izvršava. Socketio šalje poruke, a odgovorni su za poruke u određenom kanalu.
Funkcija slanja poruke dodaje novu poruku na servere, briše posljednju poruku iz pohrane ako postoj
više od 100 poruka, a zatim emitira poruku koju su primili svi klijenit na kanalu na koji je poslan.

</ P>

<h1>Osobni osvrt  </h1>
<p> Dodao sam prikazanom nazivu "superuser" posebne povlastice.Dane su im ovlasti da izbrišu bilo koji kanal i njegove komentare sa servera i iz pogleda bilo kojeg drugog korisnika koji koristi aplikaciju. Za brisanje kanala,
ime za prikaz "superuser" mora biti u kanalu koji želi izbrisati i upisati "command delete {channel name here}".
Kada superuser to učini, svi korisnici koji koriste aplikaciju maknu se s bilo kojeg kanala u kojem se nalaze i premještaju u opći, zajedno sa superuserom.Dobiva se poruka o tom koji je kanal superuser upravo izbrisao. Bez
mogućnosti kao što je ova jedini način za brisanje kanala bio bi ponovno pokretanje servera.
</ P>
