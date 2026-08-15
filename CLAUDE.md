# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The **GitHub profile repository** for `devty` (Tyler Singletary). Because the repository name
matches the account name, `README.md` renders at <https://github.com/devty> above the pinned
repositories. There is no application code, build system, or test suite — do not invent a
toolchain. **This file is public too.**

The README's job is *proof of work*: it leads with contributions merged into large third-party
codebases, then original projects, then shipped products, then career history. Preserve that
order when editing — it is the page's argument, not an arbitrary layout.

## Files

- `README.md` — the profile page
- `assets/header-{light,dark}.svg` — the banner, one per color scheme
- `assets/generate-header.py` — generates both SVGs

## Regenerating the banner

Edit `assets/generate-header.py`, never the `.svg` files directly:

```bash
python3 assets/generate-header.py       # rewrites both SVGs, byte-stable
rsvg-convert -w 880 assets/header-light.svg -o /tmp/check.png   # to eyeball it
```

Theme switching uses `<picture>` + `<source media="(prefers-color-scheme: dark)">`, which GitHub
supports in markdown. Do **not** collapse this to a single SVG with an internal `@media` block —
GitHub proxies images through its camo cache and the media query cannot be relied on to flip.

The banner's piano-roll motif uses `gradientUnits="userSpaceOnUse"` spanning the roll's x-range,
so color progresses across the phrase. Reverting to the default `objectBoundingBox` makes every
note repeat the full gradient and they all render the same flat mauve.

## Editing the README

- Anything committed here is **immediately live** on a public profile.
- A single newline inside a markdown paragraph is a soft wrap, not a line break. Multi-entry
  blocks need real structure (`####` headings or list syntax) — not trailing double-spaces,
  which are invisible and get stripped.
- **Verify repository visibility before citing anything.** Most of the owner's current work lives
  in private repos, and `gh search prs --author devty` runs authenticated, so it returns private
  results that must never reach this page. Check each one first:
  ```bash
  gh api repos/<owner>/<name> --jq .visibility   # must print "public"
  ```
  Private work may still be described when the product itself is public and already documented on
  <https://tyler.singletary-kodysh.com> — name the shipped product and its live URL, never the repo.
- Career figures (ARR, latency, precision/recall, dates) come from the portfolio site, which is the
  source of truth. Do not invent or round them further.

## Facts that go stale

Star counts in the README are **hardcoded snapshots taken 2026-08-15** (`garrytan/gbrain` 28,465 →
"28.5k"; `santifer/career-ops` 63,892 → "63.9k"). Refresh them when editing nearby:

```bash
gh api repos/garrytan/gbrain --jq .stargazers_count
gh api repos/santifer/career-ops --jq .stargazers_count
```

The open PR `santifer/career-ops#824` is described as open — re-check its state before publishing:

```bash
gh api repos/santifer/career-ops/pulls/824 --jq '{state, merged}'
```
