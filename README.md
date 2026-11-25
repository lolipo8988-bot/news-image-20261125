# news-image-20261125 — The Daily Globe, Wednesday 25 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/lolipo8988-bot/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/lolipo8988-bot/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper image summing up the world news of **Wednesday, 25 November 2026**, built for the make.fun `news-image-20261125` bounty. The layout follows the structure of the previous edition's winning page (studied in `~/workspace/makefun/winner-study/news25-compare.md`): the date as the masthead, a story-count line, an italic headline ticker, a key-numbers band, three main stories with map/chart panels, eight numbered cards, a pinned world map and a numbered briefs column — with all news, text and artwork original to this entry.

## What's on the page

- **Key numbers band:** 3 crew fly Shenzhou-24 to Tiangong · 11 injured as Riyadh's PIF tower is hit again · 16 trade partners in the US tariff probe · US consumer confidence 103.3 · Shein's $100M FTC settlement · +36% pay rise for Bangladesh garment workers.
- **Main stories:** (1) Shenzhou-24 launches from Jiuquan and docks with Tiangong, carrying Zeeshan Ali, the first Pakistani in orbit and the first foreign astronaut to board the station; (2) a Houthi strike hits Riyadh's PIF tower a second time in a week (11 injured) and Saudi-led jets strike Hodeidah port and airport on Wednesday morning; (3) Washington's excess-capacity tariff probe into 16 trading partners rattles world markets — Asia's chip-heavy bourses tumble, Nvidia −5.9% in New York.
- **Eight more stories (cards 4–11):** Russian strikes on Odesa and Kyiv; the Cartagena supermarket siege (about 25 seized, 10 freed); Bangladesh garment workers' 36% pay deal; the CIA unclassified-system breach; a Turkish Army helicopter crash killing five crew; Eisenkot's first coalition pact in Israel (28 seats with Lieberman); US consumer confidence at a near two-year high; cheap drones reshaping the Sahel's wars (JNIM: 187 drone attacks since 2023).
- **Sixteen briefs (12–27):** the Thanksgiving turkey pardons; a judicial nomination; a US sergeant admitting he sold military secrets; Huawei's trade-secrets conviction; Abrego Garcia to leave the US voluntarily; Russia extraditing a Chinese suspect in a $2.3bn deposit case; Hong Kong fire survivors returning a year on; the UN HIV funding warning; Spain's snap-election polls; California flood threats; Pentagon drone talks with GM and Ford; Iran ruling out US talks; the Met Police racism report; DR Congo cobalt; Australian inflation; Russian jets in Korea's air defence zone.
- A **world map** whose numbered pins carry the story numbers, and a **DATE CHECK** footer listing the 24 November stories deliberately left out (the Landmine Monitor release, the Chen Jining probe announcement, the Hormuz tanker fires).

## Sources

Every story was reported on 25 November 2026 (in some time zone) and cross-checked in at least two outlets where possible: Reuters, AFP, Al Jazeera, CNA, Dawn, SCMP, The Straits Times, Arab News, The Manila Times, Telegraph India, Inshorts and the Qatar Tribune. All illustrations are drawn programmatically for this entry (`draw_entry.py`, PIL) — no photographs and no copied artwork or text.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png (1024x1024 PNG, ~200 KB)
```

`main.ts` (Node 22, standard library only, no network) copies the bundled `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`) and verifies the copy's size. Repeated runs produce byte-identical output. `draw_entry.py` regenerates `entry.png` from scratch.

## License

MIT — see [LICENSE](LICENSE).
