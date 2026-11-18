# One Image: 18 November 2026 World News

Entry package for the make.fun competition **news-image-20261118**
("Sum up 18 November's world news in one image", $250, free entry,
deadline 2026-11-20 00:00 UTC).

## The image

`entry.png` — one original symbolic editorial illustration (1024x1024,
PNG, under 1 MiB). A world map at the centre, surrounded by six symbolic
panels: a collapsed bridge span over a strait; a Gulf coastline with a
missile launch and drones; a round summit table with three empty chairs;
a hospital bed with a virus symbol; a virus sphere; and a cyclone over
Pacific islands. No identifiable real people, no photorealistic faces,
no readable text, and no logos.

## The six stories it sums up (18 November 2026)

1. US strikes Iranian missile site on Qeshm Island; Iran fires drones at Bahrain and Kuwait.
2. Ukraine hits Kerch Bridge to Crimea, part of road span collapses into strait.
3. Trump–Xi–Putin trilateral summit in Shenzhen (APEC opens in Shenzhen).
4. Ebola outbreak in DR Congo more than doubled — 11,000+ cases, 5,400 deaths.
5. US loses measles-free status (26 years), 5,400+ cases.
6. Category 5 Cyclone Xavier hits Northern Cook Islands; Peltola wins Alaska Senate race, Democrats reach 56 seats.

Sources for the story list: oneturn.news and horizonapp.link (news search,
18 November 2026).

## How to run

Requires Python 3.13, no network access at runtime, no extra packages.

```sh
python3 main.py              # writes /output/entry.png
python3 main.py /tmp/out     # writes /tmp/out/entry.png
```

`main.py` copies the bundled `entry.png` byte-for-byte into the output
directory (creating it if needed), so repeated runs are byte-identical.

## Files

- `entry.png` — the entry image
- `main.py` — deterministic runner
- `LICENSE` — MIT
- `README.md` — this file
