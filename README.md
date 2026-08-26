<div align="center">
  <img alt="Sverre — building AI systems, fundamentals first" width="100%"
       src="https://raw.githubusercontent.com/hellosverre/hellosverre/main/assets/banner.svg">
</div>

<div align="center">
  <a href="mailto:snorre@addmedia.no"><img alt="Email" src="https://img.shields.io/badge/snorre%40addmedia.no-081A10?style=flat-square&logo=maildotru&logoColor=76D5A1&labelColor=081A10"></a>
  &nbsp;
  <a href="https://github.com/hellosverre?tab=repositories"><img alt="Repositories" src="https://img.shields.io/badge/repositories-081A10?style=flat-square&logo=github&logoColor=76D5A1&labelColor=081A10"></a>
  &nbsp;
  <img alt="Based in Ski, Norway" src="https://img.shields.io/badge/Ski%2C%20Norge-081A10?style=flat-square&logo=googlemaps&logoColor=76D5A1&labelColor=081A10">
  &nbsp;
  <img alt="Open to apprenticeship from August 2027" src="https://img.shields.io/badge/l%C3%A6replass-aug%202027-76D5A1?style=flat-square&labelColor=081A10">
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
> **Ser etter læreplass fra august 2027** — IT-utviklerfaget eller IT-driftsfaget, i Ski/Oslo-området.
> Går Vg2 Informasjonsteknologi nå og skal ta fagbrev. Har kodet i flere år og driftet egen server i over ett år.
> Er du lærebedrift, eller kjenner du en? **[Ta kontakt →](mailto:snorre@addmedia.no)**

---

## Public repos

The MCP servers came out of a stretch of digging into how AI clients actually talk to external
systems. Not where my attention is now, but they still run and they still work.

#### [`brreg-mcp`](https://github.com/hellosverre/brreg-mcp) <sub>JavaScript · MIT</sub>

Company lookup against **Enhetsregisteret**: organisasjonsnummer, roles, subunits, live updates.
Ask an AI client who sits on a board and it answers from the register rather than from memory.

#### [`kartverket-mcp`](https://github.com/hellosverre/kartverket-mcp) <sub>JavaScript · MIT</sub>

Norwegian **addresses, place names and elevation** from Kartverket's open APIs.
Geocoding and høydedata without signing up for anything.

#### [`discord-ts-template`](https://github.com/hellosverre/discord-ts-template) <sub>TypeScript</sub>

The discord.js v14 boilerplate I got tired of rewriting. Dynamic command and event loading,
cooldowns, permission gates, context menus, autocomplete, hot reload.

---

## Also built

Private repos. Happy to walk through any of them, or give a lærebedrift read access.

| Project | What it is | Stack |
|---|---|---|
| **krait** | Licensed desktop product — storefront, auth, and a licensing/entitlement API | Next.js 16 · Tailwind 4 · Better Auth + TOTP · Drizzle/libSQL |
| **aether** | Analytics for ER:LC server owners — dashboard plus API on a VM behind a Cloudflare Tunnel | Next.js 15 · Hono · Drizzle · Postgres · Redis |
| **tnrp** | Community platform: marketing site, dashboard, leaderboard, verification flow, moderation and economy bot, click-through staff HUD | Next.js 16 · discord.js · Tauri 2 |
| **erlc.cc** | Verified staff résumé service — portable reputation across servers | Next.js · TypeScript |
| **portfolio** | Personal site, raw CSS variables, working ⌘K palette | Next.js 15 · TypeScript |

---

## Stack

<sub>**WRITE**</sub><br>
![TypeScript](https://img.shields.io/badge/TypeScript-081A10?style=flat-square&logo=typescript&logoColor=76D5A1&labelColor=081A10)
![JavaScript](https://img.shields.io/badge/JavaScript-081A10?style=flat-square&logo=javascript&logoColor=76D5A1&labelColor=081A10)
![Node.js](https://img.shields.io/badge/Node.js-081A10?style=flat-square&logo=nodedotjs&logoColor=76D5A1&labelColor=081A10)
![Python](https://img.shields.io/badge/Python-081A10?style=flat-square&logo=python&logoColor=76D5A1&labelColor=081A10)

<sub>**BUILD**</sub><br>
![Next.js](https://img.shields.io/badge/Next.js-081A10?style=flat-square&logo=nextdotjs&logoColor=76D5A1&labelColor=081A10)
![React](https://img.shields.io/badge/React-081A10?style=flat-square&logo=react&logoColor=76D5A1&labelColor=081A10)
![Hono](https://img.shields.io/badge/Hono-081A10?style=flat-square&logo=hono&logoColor=76D5A1&labelColor=081A10)
![Tailwind](https://img.shields.io/badge/Tailwind-081A10?style=flat-square&logo=tailwindcss&logoColor=76D5A1&labelColor=081A10)
![Tauri](https://img.shields.io/badge/Tauri-081A10?style=flat-square&logo=tauri&logoColor=76D5A1&labelColor=081A10)
![MCP](https://img.shields.io/badge/Model%20Context%20Protocol-081A10?style=flat-square&logo=anthropic&logoColor=76D5A1&labelColor=081A10)

<sub>**STORE**</sub><br>
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-081A10?style=flat-square&logo=postgresql&logoColor=76D5A1&labelColor=081A10)
![libSQL](https://img.shields.io/badge/libSQL-081A10?style=flat-square&logo=sqlite&logoColor=76D5A1&labelColor=081A10)
![Redis](https://img.shields.io/badge/Redis-081A10?style=flat-square&logo=redis&logoColor=76D5A1&labelColor=081A10)
![Drizzle](https://img.shields.io/badge/Drizzle-081A10?style=flat-square&logo=drizzle&logoColor=76D5A1&labelColor=081A10)

<sub>**RUN**</sub><br>
![Linux](https://img.shields.io/badge/Linux-081A10?style=flat-square&logo=linux&logoColor=76D5A1&labelColor=081A10)
![Docker](https://img.shields.io/badge/Docker-081A10?style=flat-square&logo=docker&logoColor=76D5A1&labelColor=081A10)
![Cloudflare Tunnel](https://img.shields.io/badge/Cloudflare%20Tunnel-081A10?style=flat-square&logo=cloudflare&logoColor=76D5A1&labelColor=081A10)
![Vercel](https://img.shields.io/badge/Vercel-081A10?style=flat-square&logo=vercel&logoColor=76D5A1&labelColor=081A10)
![Proxmox](https://img.shields.io/badge/Home%20server-081A10?style=flat-square&logo=proxmox&logoColor=76D5A1&labelColor=081A10)

---

<div align="center">
  <sub>Building an AI system that has to survive contact with real users?</sub><br>
  <a href="mailto:snorre@addmedia.no"><b>snorre@addmedia.no</b></a>
</div>
