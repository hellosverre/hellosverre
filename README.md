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

The other half is deliberate and slower: **learning the fundamentals properly**. AI makes it very
easy to ship code you cannot debug. I use it hard, every day, but I read what it writes and I want
to understand the layer underneath it — how these models actually arrive at an answer, what makes
one prompt hold up and another fall over. Otherwise you are not building anything, you are just
moving the bug somewhere you cannot see it.

> [!NOTE]
> **Looking for an apprenticeship from August 2027** — *IT-utviklerfaget* or *IT-driftsfaget*, in the Ski/Oslo area.
> Currently in Vg2 Informasjonsteknologi, heading for a *fagbrev*. Several years of coding, and a home server I have run for over a year.
> Are you a *lærebedrift*, or do you know one? **[Get in touch →](mailto:sverresig@proton.me)**

<br>

## Stack

<div align="center">
  <img alt="Stack: TypeScript, JavaScript, Python, Next.js, React, Hono, Tailwind, Tauri, Postgres, libSQL, Redis, Drizzle, Linux, Docker, Cloudflare Tunnel, Vercel, Proxmox"
       width="100%"
       src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/stack.svg">
</div>

<br>

## Public repos

The MCP servers came out of a stretch of digging into how AI clients actually talk to external
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

| Project | What it is | Stack |
|---|---|---|
| **krait** | Licensed desktop product — storefront, auth, and a licensing/entitlement API | Next.js 16 · Tailwind 4 · Better Auth + TOTP · Drizzle/libSQL |
| **aether** | Analytics for ER:LC server owners — dashboard plus API on a VM behind a Cloudflare Tunnel | Next.js 15 · Hono · Drizzle · Postgres · Redis |
| **tnrp** | Community platform: marketing site, dashboard, leaderboard, verification flow, moderation and economy bot, click-through staff HUD | Next.js 16 · discord.js · Tauri 2 |
| **erlc.cc** | Verified staff résumé service — portable reputation across servers | Next.js · TypeScript |
| **portfolio** | Personal site, raw CSS variables, working ⌘K palette | Next.js 15 · TypeScript |

<br>

<div align="center">
  <a href="mailto:sverresig@proton.me">
    <img alt="Get in touch — sverresig@proton.me" width="100%"
         src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/footer-en.svg">
  </a>
</div>
