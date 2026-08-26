<!-- Panelene er generert: python tools/build.py
     Denne fila og README.md er det samme dokumentet på to språk. Hold dem synkronisert. -->

<div align="center">
  <a href="https://github.com/hellosverre"><img alt="English" height="36" src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/lang-en-off.svg"></a>
  <img alt="Norsk" height="36" src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/lang-no-on.svg">
</div>

<div align="center">
  <img alt="Sverre — bygger AI-systemer, grunnprinsipper først" width="100%"
       src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/banner-no.svg">
</div>

<div align="center">
  <a href="mailto:sverresig@proton.me"><img alt="E-post" src="https://img.shields.io/badge/sverresig%40proton.me-081A10?style=flat-square&logo=protonmail&logoColor=76D5A1&labelColor=081A10"></a>
  &nbsp;
  <a href="https://github.com/hellosverre?tab=repositories"><img alt="Repoer" src="https://img.shields.io/badge/repoer-081A10?style=flat-square&logo=github&logoColor=76D5A1&labelColor=081A10"></a>
  &nbsp;
  <img alt="Basert i Ski, Norge" src="https://img.shields.io/badge/Ski%2C%20Norge-081A10?style=flat-square&logo=googlemaps&logoColor=76D5A1&labelColor=081A10">
  &nbsp;
  <img alt="Åpen for læreplass fra august 2027" src="https://img.shields.io/badge/l%C3%A6replass-aug%202027-76D5A1?style=flat-square&labelColor=081A10">
</div>

<br>

## `whoami`

Jeg lager **verktøy som fjerner friksjonen i arbeid jeg gjør om og om igjen**. Hvis noe koster meg en
time to ganger, blir det et produkt. De fleste starter som noe jeg trengte klokka to om natta, og
slippes først når de har overlevd et par uker med at jeg faktisk bruker dem.

Mesteparten av oppmerksomheten min går nå til **AI-systemer** — laget som ligger mellom en modell
og faktisk arbeid. Orkestrering, konteksthåndtering, ruting av verktøy, og det å vite hvor en modell
kommer til å ta feil i det stille, slik at du får bygget kontrollen som fanger det opp før en bruker gjør det.

Den andre halvdelen er bevisst og tregere: **å lære grunnprinsippene ordentlig**. AI gjør det veldig
lett å sende fra seg kode du ikke klarer å feilsøke. Jeg bruker det hardt, hver dag, men jeg leser
det som blir skrevet, og jeg vil forstå laget under — hvordan disse modellene faktisk kommer fram
til et svar, hva som gjør at én prompt holder og en annen ryker. Ellers bygger du ingenting, du
flytter bare feilen dit du ikke ser den.

> [!NOTE]
> **Ser etter læreplass fra august 2027** — IT-utviklerfaget eller IT-driftsfaget, i Ski/Oslo-området.
> Går Vg2 Informasjonsteknologi nå og skal ta fagbrev. Har kodet i flere år og driftet egen server i over ett år.
> Er du lærebedrift, eller kjenner du en? **[Ta kontakt →](mailto:sverresig@proton.me)**

<br>

## Stack

<div align="center">
  <img alt="Stack: TypeScript, JavaScript, Python, Next.js, React, Hono, Tailwind, Tauri, Postgres, libSQL, Redis, Drizzle, Linux, Docker, Cloudflare Tunnel, Vercel"
       width="100%"
       src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/stack.svg">
</div>

<br>

## Åpen kildekode

#### [`slab`](https://github.com/hellosverre/slab) <sub>Python · MIT · <code>pip install slabkit</code></sub>

Panelsystemet denne profilen er bygget på. Palettene utledes i OKLCH fra én fargetone og
**sjekker sine egne kontrastforhold**, så et uleselig tema feiler når det bygges i stedet for å bli
publisert. Superellipse-hjørner, filmkorn, én bevegelse per panel — alt bygget innenfor det GitHub
faktisk rendrer, der `<style>` blir gjort om til ren tekst og webfonter aldri lastes.

MCP-serverne under kom ut av en periode der jeg gravde i hvordan AI-klienter faktisk snakker med
eksterne systemer. Ikke der oppmerksomheten min er nå, men de kjører fortsatt og de virker fortsatt.

#### [`brreg-mcp`](https://github.com/hellosverre/brreg-mcp) <sub>JavaScript · MIT</sub>

Oppslag mot **Enhetsregisteret**: organisasjonsnummer, roller, underenheter, oppdateringer.
Spør en AI-klient hvem som sitter i et styre, og den svarer fra registeret i stedet for fra hukommelsen.

#### [`kartverket-mcp`](https://github.com/hellosverre/kartverket-mcp) <sub>JavaScript · MIT</sub>

Norske **adresser, stedsnavn og høydedata** fra Kartverkets åpne API-er.
Geokoding og høydedata uten å registrere seg for noe.

#### [`discord-ts-template`](https://github.com/hellosverre/discord-ts-template) <sub>TypeScript</sub>

discord.js v14-malen jeg ble lei av å skrive på nytt. Dynamisk lasting av kommandoer og events,
cooldowns, tilgangsstyring, kontekstmenyer, autocomplete, hot reload.

<br>

## Også bygget

Private repoer. Jeg går gjerne gjennom hvilket som helst av dem, eller gir en lærebedrift lesetilgang.

| Prosjekt | Hva det er | Stack |
|---|---|---|
| **krait** | Lisensiert desktop-produkt — nettbutikk, innlogging og et API for lisenser og rettigheter | Next.js 16 · Tailwind 4 · Better Auth + TOTP · Drizzle/libSQL |
| **aether** | Analyse for ER:LC-servereiere — dashbord og API på en VM bak en Cloudflare Tunnel | Next.js 15 · Hono · Drizzle · Postgres · Redis |
| **tnrp** | Community-plattform: nettside, dashbord, ledertavle, verifiseringsflyt, moderasjons- og økonomibot, klikk-gjennom HUD for staff | Next.js 16 · discord.js · Tauri 2 |
| **erlc.cc** | Verifisert staff-CV — omdømme du tar med deg mellom servere | Next.js · TypeScript |
| **portfolio** | Personlig nettside, rene CSS-variabler, fungerende ⌘K-palett | Next.js 15 · TypeScript |

<br>

**aether** er den jeg kan vise formen på uten å vise koden:

<div align="center">
  <img alt="aether-arkitektur: nettleser til Vercel til Cloudflare Tunnel til en VM med Hono og Drizzle, med Postgres og Redis bak"
       width="100%" src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/architecture-no.svg">
</div>

<br>

<div align="center">
  <a href="mailto:sverresig@proton.me">
    <img alt="Ta kontakt — sverresig@proton.me" width="100%"
         src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/footer-no.svg">
  </a>
</div>
