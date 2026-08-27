<!-- Panels are generated: python tools/build.py
     This file and README.no.md are the same document in two languages. Keep them in sync. -->

<div align="center">
  <img alt="English" height="36" src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/lang-en-on.svg">
  <a href="https://github.com/hellosverre/hellosverre/blob/main/README.no.md"><img alt="Norsk" height="36" src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/lang-no-off.svg"></a>
</div>

<div align="center">
  <img alt="Sverre — building AI systems, fundamentals first" width="100%"
       src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/banner-en.svg">
</div>

<div align="center">
  <a href="mailto:sverresig@proton.me"><img alt="Email" src="https://img.shields.io/badge/sverresig%40proton.me-081A10?style=flat-square&logo=protonmail&logoColor=76D5A1&labelColor=081A10"></a>
  &nbsp;
  <a href="https://github.com/hellosverre?tab=repositories"><img alt="Repositories" src="https://img.shields.io/badge/repositories-081A10?style=flat-square&logo=github&logoColor=76D5A1&labelColor=081A10"></a>
  &nbsp;
  <img alt="Based in Ski, Norway" src="https://img.shields.io/badge/Ski%2C%20Norway-081A10?style=flat-square&logo=googlemaps&logoColor=76D5A1&labelColor=081A10">
  &nbsp;
  <img alt="Open to apprenticeship from August 2027" src="https://img.shields.io/badge/apprenticeship-aug%202027-76D5A1?style=flat-square&labelColor=081A10">
</div>

<br>

## `whoami`

I build **tools that take the friction out of work I do repeatedly**. If something costs me an hour
twice, it turns into a product. Most of them start as something I needed at 2am and only get
released once they survive a few weeks of me actually using them.

Most of my attention right now goes to **AI systems** — the layer that sits between a model and
real work. Orchestration, context handling, tool routing, and knowing where a model will quietly
get something wrong so you can build the check that catches it before a user does.

The other half is deliberate and slower: **the layer underneath**. AI makes it very easy to ship
code you cannot debug, so I keep the habit of going one level below what a job strictly needs —
[`hotpath`](https://github.com/hellosverre/hotpath) is where that happens, and not one number in it
is remembered from someone's blog. I use AI hard, every day. Being able to tell when it is wrong is
the entire reason the fundamentals are worth the time — otherwise you are not building anything,
you are just moving the bug somewhere you cannot see it.

> [!NOTE]
> **Looking for an apprenticeship from August 2027** — *IT-utviklerfaget* or *IT-driftsfaget*, in the Ski/Oslo area.
> Currently in Vg2 Informasjonsteknologi, heading for a *fagbrev*. I have been writing code for years — this
> account is new because most of that work lived locally or in private repos. Three packages published
> (two on npm, one on PyPI), and a home server I ran for over a year.
> Are you a *lærebedrift*, or do you know one? **[Get in touch →](mailto:sverresig@proton.me)**

<br>

## Stack

<div align="center">
  <img alt="Stack: TypeScript, JavaScript, Python, Next.js, React, Hono, Tailwind, Tauri, Postgres, libSQL, Redis, Drizzle, Linux, Docker, Cloudflare Tunnel, Vercel"
       width="100%"
       src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/stack.svg">
</div>

<br>

## Public repos

#### [`hotpath`](https://github.com/hellosverre/hotpath) <sub>Rust · MIT</sub>

Faster versions of ordinary things, with the measurement to back it up. Counting newlines seven
ways — naive, SWAR, `memchr`, `bytecount`, hand-written AVX2 behind a runtime feature check, threaded
— measured against what a single core can pull from memory, so it is obvious at which point the code
stopped being the bottleneck. Every entry needs a baseline, a named mechanism and error bars, and
**the results table is generated from `criterion` output rather than typed by hand**. The losses get
published too: a table of nothing but wins is a table nobody should believe.

#### [`slab`](https://github.com/hellosverre/slab) <sub>Python · MIT · <code>pip install slabkit</code></sub>

The panel system this profile is built on. Palettes are derived in OKLCH from a single hue and
**assert their own contrast ratios**, so an unreadable theme fails at build time instead of shipping.
Superellipse corners, film grain, one motion idea per panel — all of it built inside GitHub's actual
rendering envelope, where `<style>` is escaped to plain text and webfonts never load.

The MCP servers below came out of a stretch of digging into how AI clients actually talk to external
systems. Not where my attention is now, but they still run and they still work.

#### [`brreg-mcp`](https://github.com/hellosverre/brreg-mcp) <sub>JavaScript · MIT</sub>

Company lookup against **Enhetsregisteret**, the Norwegian business register: organisation numbers,
roles, subunits, live updates. Ask an AI client who sits on a board and it answers from the register
rather than from memory.

#### [`kartverket-mcp`](https://github.com/hellosverre/kartverket-mcp) <sub>JavaScript · MIT</sub>

Norwegian **addresses, place names and elevation** from the open APIs of Kartverket, the national
mapping authority. Geocoding and elevation data without signing up for anything.

#### [`discord-ts-template`](https://github.com/hellosverre/discord-ts-template) <sub>TypeScript</sub>

The discord.js v14 boilerplate I got tired of rewriting. Dynamic command and event loading,
cooldowns, permission gates, context menus, autocomplete, hot reload.

<br>

## Also built

Private repos. Happy to walk through any of them, or give a *lærebedrift* read access.
**vellum** is the one with the process on show — every feature lands as a reviewed pull request against a numbered ADR.

| Project | What it is | Stack |
|---|---|---|
| **vellum** | Discord automation platform — visual flow builder, durable job runner, and a copilot that writes the flows | Next.js · discord.js · Drizzle |
| **krait** | Licensed desktop product — storefront, auth, and a licensing/entitlement API | Next.js 16 · Tailwind 4 · Better Auth + TOTP · Drizzle/libSQL |
| **aether** | Analytics for ER:LC server owners — dashboard plus API on a VM behind a Cloudflare Tunnel | Next.js 15 · Hono · Drizzle · Postgres · Redis |
| **tnrp** | Community platform: marketing site, dashboard, leaderboard, verification flow, moderation and economy bot, click-through staff HUD | Next.js 16 · discord.js · Tauri 2 |
| **erlc.cc** | Verified staff résumé service — portable reputation across servers | Next.js · TypeScript |
| **portfolio** | Personal site, raw CSS variables, working ⌘K palette | Next.js 15 · TypeScript |

<br>

**aether** is the one whose shape I can show without showing the code:

<div align="center">
  <img alt="aether architecture: browser to Vercel to Cloudflare Tunnel to a VM running Hono and Drizzle, backed by Postgres and Redis"
       width="100%" src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/architecture-en.svg">
</div>

<br>

<div align="center">
  <a href="mailto:sverresig@proton.me">
    <img alt="Get in touch — sverresig@proton.me" width="100%"
         src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/footer-en.svg">
  </a>
</div>
