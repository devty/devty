<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img alt="Tyler Singletary — Music · Code · ML and AI — Brooklyn, NY" src="assets/header-light.svg" width="880">
</picture>

**Developer experience as product.** Twenty years building platforms that other people build on — API ecosystems, developer tooling, and now the infrastructure underneath AI agents. Currently independent, shipping under **@orchestrately**.

---

### Shipped into other people's codebases

#### [garrytan/gbrain](https://github.com/garrytan/gbrain) · ★ 30.5k

Four issues filed, all four closed as fixed. Fix for the last one merged as [#3701](https://github.com/garrytan/gbrain/pull/3701).

- A drain worker [self-deadlocking at `concurrency=1`](https://github.com/garrytan/gbrain/issues/2050), stalling any cycle phase that spawned a subagent
- [Owner identity fragmenting](https://github.com/garrytan/gbrain/issues/2465) across three different holder strings
- A [calibration default that silently no-op'd forecasting](https://github.com/garrytan/gbrain/issues/2464) on every non-owner brain
- A [cycle phase hardcoded to `source=default`](https://github.com/garrytan/gbrain/issues/3679), never scoped to the resolved id

#### [career-ops](https://github.com/career-ops-hq/career-ops) · ★ 73.2k

- Fixed a [merge-tracker regex](https://github.com/career-ops-hq/career-ops/issues/2925) that never matched the documented inline `**URL:**` header, leaving URL dedup silently inactive. Merged as [#2926](https://github.com/career-ops-hq/career-ops/pull/2926).
- [#824](https://github.com/career-ops-hq/career-ops/pull/824), open — `create-a-role` "gambit" mode and Speculative pipeline state.

### Open source of mine

#### [extract-scout](https://github.com/devty/rails-exscout-plugin)

A Claude Code plugin that scouts a Rails monolith and reports how entangled a domain is and which seams must break before it can be extracted. Cites every claim and says what it didn't look at. No dependencies beyond Ruby's stdlib.

#### [mtplx-dashboard](https://github.com/devty/mtplx-dashboard)

Realtime dashboard and activity log for local LLM inference on Apple Silicon. A small TypeScript server polls MTPLX's `/metrics` and streams to the browser over SSE; the frontend is four plain HTML files — no client framework, no build step. Surfaces the part of speculative decoding that actually matters: tokens per verify pass, per-depth acceptance, throughput, cache health.

#### [MidiTok](https://github.com/devty/MidiTok)

`StructuredREMI` and MuMIDI tokenizers extended to carry MIDI control-change data. The public edge of **Ravel AI** — an AI-first DAW that generates expressive MIDI: the dynamics, articulation, and phrasing that make a part sound played rather than entered.

#### [cohere-decisions](https://github.com/devty/cohere-decisions)

Retrieval over an organizational decision log, so "can we accept NET120 terms?" gets answered from the record instead of from memory.

### Built privately, live publicly

- **[Famlore](https://famlore.app)** — A game of inquiry that runs through the AI client you already use: it keeps the record of what you're furthest into and hands you one specific thing to go find out. Next.js and Supabase, an MCP server, and a [Claude plugin](https://github.com/devty/famlore-plugin).
- **[Colophon](https://orchestrately.com)** *(pre-release)* — A macOS catalog for every sample library you own. Reads Kontakt, SINE and Audio Unit installs into one searchable index, queryable from the app or from your AI assistant over MCP.
- **[Sylvaness](https://sylvaness.devtysingletary.workers.dev/)** *(building)* — A playable study of a living forest: trees grown by space colonization with seasonal leaves, no imported models. One deterministic simulation drives a Three.js build and a native SwiftUI/Metal prototype.
- **[Stockstead](https://www.stockstead.com)** — Mortgage modeling for the cases standard calculators refuse: SBLOCs, tax-loss harvesting, portfolio-backed lending.
- **[Timeblind](https://www.timeblind.today)** — Visual time-blocking for when ADHD makes the clock invisible. Gentle nudges, not guilt-trips.
- **[Forbearance](https://forbearance.fun)** — A word game that teaches you to do without.
- **Historic** — Walk up to a landmark, get an AI-narrated podcast on the spot. Fine-tuned Gemma 3 on-device, Swift and AR on top.

### Before this

- **Klout** *(2011–2016)* — Built the developer platform from zero to 7-figure ARR and 60% of company revenue; API latency from hundreds of milliseconds to ~12ms. Exit to Lithium, where I ran Klout and consumer data as VP/GM.
- **Tagboard** *(2016–2024)* — CPO through the turnaround. ARR $600K → $7.2M, churn 65% → 8%, seven products onto one platform.
- **Canvs AI** *(2018–2019)* — Rebuilt emotion and topic models from ~70% to ~85% precision/recall.
- **AWS** *(2024–2026)* — AI/ML startups. GenAI and small-model playbooks for LoRA fine-tuning and evaluation, used by founders and field teams.

Talks at APIDays NYC (2026, *How AI Learned To Stop Worrying And Love The Scrape*), APIDays Paris, API Strategy & Practice, and The Business of APIs.

---

[Portfolio](https://tyler.singletary-kodysh.com) · [Substack](https://tylersingletary.substack.com) · [LinkedIn](https://linkedin.com/in/tyler-singletary) · [@harmophone](https://x.com/harmophone)
