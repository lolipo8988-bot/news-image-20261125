#!/usr/bin/env python3
"""The Daily Globe - Wednesday 25 November 2026 (make.fun news-image-20261125).

Original PIL drawing for this edition only: masthead, numbers band, three
map/chart main panels, eight numbered cards, a pinned world map and a
numbered briefs column. All text and art written/drawn for this file.
"""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFont

NOTO = "/usr/share/fonts/truetype/noto"
SERIF_B = f"{NOTO}/NotoSerif-Bold.ttf"
SERIF = f"{NOTO}/NotoSerif-Regular.ttf"
SERIF_I = f"{NOTO}/NotoSerif-Italic.ttf"
SANS = f"{NOTO}/NotoSans-Regular.ttf"
SANS_B = f"{NOTO}/NotoSans-Bold.ttf"

W = H = 1024
M = 28
CW = W - 2 * M
PAPER = (247, 242, 231)
INK = (26, 23, 18)
RED = (179, 53, 43)
GRAY = (110, 102, 90)
RULE = (60, 54, 44)

REG = {
    "EUROPE": (43, 94, 167),
    "MIDDLE EAST": (179, 53, 43),
    "ASIA": (122, 79, 163),
    "AFRICA": (192, 122, 30),
    "AMERICAS": (30, 122, 90),
    "OCEANIA": (42, 138, 158),
    "WORLD": (96, 90, 80),
}

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def F(path, size):
    return ImageFont.truetype(path, size)


def tw(text, font):
    return d.textlength(text, font=font)


def fit(text, path, size, max_w, min_size=9):
    s = size
    while s > min_size and tw(text, F(path, s)) > max_w:
        s -= 1
    return F(path, s)


def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(t, font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def center(text, y, font, color=INK):
    d.text(((W - tw(text, font)) / 2, y), text, font=font, fill=color)


def hline(y, x0=M, x1=W - M, color=RULE, wdt=1):
    d.line([(x0, y), (x1, y)], fill=color, width=wdt)


def badge(cx, cy, num, color, r=10):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    f = F(SANS_B, 11)
    t = str(num)
    d.text((cx - tw(t, f) / 2, cy - 8), t, font=f, fill=(255, 255, 255))


# ---------------------------------------------------------------- top strip
f_strip = F(SANS_B, 11)
d.text((M, 12), "THE DAILY GLOBE", font=f_strip, fill=INK)
mid = "DAY 329 OF 2026"
d.text(((W - tw(mid, f_strip)) / 2, 12), mid, font=f_strip, fill=RED)
rgt = "EVERY STORY DATED WEDNESDAY 25 NOV"
d.text((W - M - tw(rgt, f_strip), 12), rgt, font=f_strip, fill=INK)
hline(32, wdt=2)

# ---------------------------------------------------------------- masthead
f_mast = fit("Wednesday 25 November 2026", SERIF_B, 66, CW)
center("Wednesday 25 November 2026", 40, f_mast)
hline(112, wdt=1)
stats = ("27 STORIES, ALL FROM WEDNESDAY 25 NOV  ·  EUROPE 6  ·  MIDDLE EAST 3  ·  "
         "ASIA 4  ·  AFRICA 2  ·  AMERICAS 11  ·  OCEANIA 1")
center(stats, 118, fit(stats, SANS_B, 12, CW), INK)
hline(138, wdt=2)

# ---------------------------------------------------------------- ticker
tick = ("First foreign astronaut boards Tiangong", "Riyadh tower hit again; "
        "Saudi jets strike Hodeidah", "Tariff probe of 16 partners rattles markets")
f_tick = F(SERIF_I, 15)
seg_w = [tw(t, f_tick) for t in tick]
gap = 26
total = sum(seg_w) + gap * 2
x = (W - total) / 2
y_tick = 146
for i, t in enumerate(tick):
    d.text((x, y_tick), t, font=f_tick, fill=(52, 46, 38))
    x += seg_w[i]
    if i < 2:
        cx, cy = x + gap / 2, y_tick + 9
        d.polygon([(cx, cy - 5), (cx + 5, cy), (cx, cy + 5), (cx - 5, cy)], fill=RED)
        x += gap

# ---------------------------------------------------------------- numbers band
hline(172, wdt=1)
band = [
    ("3", "crew fly Shenzhou-24 to Tiangong"),
    ("11", "injured as Riyadh tower is hit again"),
    ("16", "trade partners in the US tariff probe"),
    ("103.3", "US consumer confidence, near 2-year high"),
    ("$100M", "Shein settlement with the US FTC"),
    ("+36%", "pay rise won by Bangladesh garment staff"),
]
col_w = CW / 6
f_num = F(SERIF_B, 31)
f_cap = F(SANS, 9)
for i, (num, cap) in enumerate(band):
    cx = M + col_w * i + col_w / 2
    d.text((cx - tw(num, f_num) / 2, 178), num, font=f_num, fill=INK)
    for j, ln in enumerate(wrap(cap, f_cap, col_w - 14)[:2]):
        d.text((cx - tw(ln, f_cap) / 2, 216 + j * 11), ln, font=f_cap, fill=(70, 63, 52))
    if i:
        d.line([(M + col_w * i, 180), (M + col_w * i, 232)], fill=(196, 186, 166), width=1)
hline(240, wdt=2)

# ---------------------------------------------------------------- main panels
def panel_space(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(18, 34, 58))
    rng = random.Random(24)
    for _ in range(46):
        sx, sy = x + rng.randint(4, w - 4), y + rng.randint(4, h - 40)
        d.point((sx, sy), fill=(220, 228, 240))
    # Gobi ground
    d.polygon([(x, y + h - 26), (x + 120, y + h - 34), (x + w, y + h - 20),
               (x + w, y + h), (x, y + h)], fill=(196, 164, 110))
    d.text((x + 8, y + h - 20), "JIUQUAN - GANSU", font=F(SANS_B, 9), fill=(60, 44, 20))
    # rocket
    rx, ry = x + 52, y + h - 38
    d.polygon([(rx, ry - 34), (rx - 8, ry - 12), (rx + 8, ry - 12)], fill=(240, 240, 238))
    d.rectangle([rx - 8, ry - 12, rx + 8, ry + 2], fill=(240, 240, 238))
    d.polygon([(rx - 5, ry + 12), (rx, ry + 3), (rx + 5, ry + 12)], fill=(240, 140, 40))
    # dashed trajectory to station
    for t_i in range(21):
        tt = t_i / 20
        px = rx + 14 + tt * (w - 130)
        py = (ry - 30) - math.sin(tt * math.pi * 0.62) * 52 + tt * 6
        if t_i % 2 == 0:
            d.ellipse([px - 1.6, py - 1.6, px + 1.6, py + 1.6], fill=(250, 205, 90))
    # Tiangong station
    sx, sy = x + w - 108, y + 22
    d.rectangle([sx, sy, sx + 34, sy + 12], fill=(225, 228, 232))
    d.rectangle([sx - 26, sy + 2, sx - 2, sy + 10], fill=(70, 110, 180))
    d.rectangle([sx + 36, sy + 2, sx + 60, sy + 10], fill=(70, 110, 180))
    d.text((sx - 30, sy + 16), "TIANGONG", font=F(SANS_B, 8), fill=(200, 214, 235))
    chip = "LIFTOFF 08:18 - DOCKED +3H 38M"
    f_chip = F(SANS_B, 8)
    cw_ = tw(chip, f_chip) + 10
    d.rectangle([x + w - cw_ - 6, y + h - 22, x + w - 6, y + h - 6], fill=(10, 20, 36))
    d.text((x + w - cw_ - 1, y + h - 18), chip, font=f_chip, fill=(250, 225, 150))


def panel_redsea(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(206, 224, 230))
    # Arabia landmass
    d.polygon([(x + 128, y), (x + w, y), (x + w, y + h), (x + 168, y + h),
               (x + 150, y + 74), (x + 118, y + 40)], fill=(222, 199, 148))
    d.text((x + 14, y + 58), "RED SEA", font=F(SERIF_I, 11), fill=(40, 90, 130))
    def dot(px, py, label, lx, ly, burst=False):
        if burst:
            for a in range(0, 360, 45):
                r1, r2 = 3, 9
                d.line([(px + r1 * math.cos(math.radians(a)), py + r1 * math.sin(math.radians(a))),
                        (px + r2 * math.cos(math.radians(a)), py + r2 * math.sin(math.radians(a)))],
                       fill=RED, width=2)
        d.ellipse([px - 3.4, py - 3.4, px + 3.4, py + 3.4], fill=INK)
        d.text((lx, ly), label, font=F(SANS_B, 9), fill=INK)
    # dashed arc Hodeidah -> Riyadh
    for t_i in range(17):
        tt = t_i / 16
        px = (x + 138) + tt * 118
        py = (y + 84) - math.sin(tt * math.pi) * 26 - tt * 22
        if t_i % 2 == 0:
            d.ellipse([px - 1.5, py - 1.5, px + 1.5, py + 1.5], fill=RED)
    dot(x + 138, y + 84, "HODEIDAH", x + 84, y + 92)
    dot(x + 196, y + 44, "JEDDAH", x + 168, y + 30)
    dot(x + 258, y + 60, "RIYADH", x + 244, y + 76, burst=True)
    chip = "2ND HIT IN A WEEK - 11 HURT"
    f_chip = F(SANS_B, 8)
    cw_ = tw(chip, f_chip) + 10
    d.rectangle([x + 6, y + h - 22, x + 6 + cw_, y + h - 6], fill=(90, 30, 24))
    d.text((x + 11, y + h - 18), chip, font=f_chip, fill=(255, 235, 220))


def panel_chart(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(251, 248, 241), outline=(196, 186, 166))
    d.text((x + 10, y + 6), "CHIP-HEAVY BOURSES TUMBLE - WORST PRINTS", font=F(SANS_B, 8.5),
           fill=GRAY)
    rows = [("KOSPI", -5.3, RED), ("TAIEX", -5.1, RED), ("NIKKEI", -2.9, RED),
            ("NASDAQ*", -1.5, (205, 110, 90)), ("DOW*", 0.9, (30, 122, 90))]
    f_lab = F(SANS_B, 9)
    for i, (name, val, colr) in enumerate(rows):
        ry = y + 24 + i * 16.5
        d.text((x + 10, ry), name, font=f_lab, fill=INK)
        bx = x + 66
        bw = abs(val) / 5.3 * 168
        if val < 0:
            d.rectangle([bx, ry + 1, bx + bw, ry + 11], fill=colr)
            vt = f"{val:.1f}%"
            d.text((bx + bw + 5, ry), vt, font=f_lab, fill=colr)
        else:
            d.rectangle([bx, ry + 1, bx + bw, ry + 11], fill=colr)
            d.text((bx + bw + 5, ry), "+0.9%", font=f_lab, fill=colr)
    d.text((x + w - 96, y + h - 14), "* US close, Tuesday", font=F(SANS, 8), fill=GRAY)


MAINS = [
    dict(n=1, reg="ASIA", topic="SPACE", panel=panel_space, date="JIUQUAN, CHINA",
         head="First foreign astronaut boards Tiangong",
         body=("Shenzhou-24 lifts off at 08:18 Beijing time and docks 3 hours 38 minutes "
               "later. Pakistani pilot Zeeshan Ali, 40, joins Tang Hongbo and Wu Yi for a "
               "week of experiments - the first Pakistani in orbit."),
         src="REUTERS - CNA - DAWN"),
    dict(n=2, reg="MIDDLE EAST", topic="WAR", panel=panel_redsea, date="RIYADH / HODEIDAH",
         head="Riyadh tower hit again; Saudi jets strike Hodeidah",
         body=("A Houthi strike hits the PIF tower in Riyadh's financial district a second "
               "time in a week, injuring 11. By Wednesday morning Saudi-led jets pound "
               "Hodeidah port and airport; the Houthis threaten Jeddah."),
         src="AFP - AL JAZEERA - SCMP"),
    dict(n=3, reg="AMERICAS", topic="TRADE", panel=panel_chart, date="WASHINGTON",
         head="Tariff probe of 16 partners rattles world markets",
         body=("Washington readies findings of its excess-capacity probe into 16 trading "
               "partners, with new duties expected. Asia's chip bourses tumble on "
               "Wednesday; on Wall Street the Nvidia rebound fades, down 5.9%."),
         src="REUTERS"),
]

PANEL_Y, PANEL_H = 250, 116
MAIN_W = (CW - 32) // 3
for i, mn in enumerate(MAINS):
    x = M + i * (MAIN_W + 16)
    colr = REG[mn["reg"]]
    mn["panel"](x, PANEL_Y, MAIN_W, PANEL_H)
    ky = PANEL_Y + PANEL_H + 6
    d.rectangle([x, ky, x + MAIN_W, ky + 19], fill=colr)
    d.text((x + 8, ky + 4), f"{mn['reg']} - {mn['topic']}", font=F(SANS_B, 10.5),
           fill=(255, 255, 255))
    badge(x + MAIN_W - 14, ky + 9, mn["n"], INK, r=9)
    d.text((x, ky + 24), mn["date"], font=F(SANS_B, 9.5), fill=RED)
    f_head = fit(mn["head"], SERIF_B, 20, MAIN_W, 15)
    hy = ky + 38
    for ln in wrap(mn["head"], f_head, MAIN_W)[:2]:
        d.text((x, hy), ln, font=f_head, fill=INK)
        hy += 23
    f_body = F(SANS, 10.5)
    by = ky + 86
    for ln in wrap(mn["body"], f_body, MAIN_W)[:4]:
        d.text((x, by), ln, font=f_body, fill=(52, 46, 38))
        by += 13.5
    d.text((x, by + 2), mn["src"], font=F(SANS_B, 8), fill=GRAY)

CARDS_Y = 534

# ---------------------------------------------------------------- small cards
def icon(kind, cx, cy, colr):
    if kind == "burst":
        for a in range(0, 360, 30):
            r1, r2 = 4, 12 if a % 60 == 0 else 8
            d.line([(cx + r1 * math.cos(math.radians(a)), cy + r1 * math.sin(math.radians(a))),
                    (cx + r2 * math.cos(math.radians(a)), cy + r2 * math.sin(math.radians(a)))],
                   fill=colr, width=2)
        d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=colr)
    elif kind == "store":
        d.rectangle([cx - 12, cy - 2, cx + 12, cy + 12], outline=colr, width=2)
        for i in range(4):
            d.polygon([(cx - 12 + i * 6, cy - 10), (cx - 6 + i * 6, cy - 10),
                       (cx - 8 + i * 6, cy - 3)], fill=colr)
        d.rectangle([cx - 3, cy + 3, cx + 3, cy + 12], fill=colr)
    elif kind == "shirt":
        d.polygon([(cx - 4, cy - 11), (cx + 4, cy - 11), (cx + 12, cy - 5), (cx + 7, cy - 1),
                   (cx + 7, cy + 12), (cx - 7, cy + 12), (cx - 7, cy - 1), (cx - 12, cy - 5)],
                  outline=colr, width=2)
    elif kind == "lock":
        d.arc([cx - 7, cy - 13, cx + 7, cy + 3], 180, 360, fill=colr, width=2)
        d.rectangle([cx - 11, cy - 4, cx + 11, cy + 12], outline=colr, width=2)
        d.ellipse([cx - 2.4, cy + 1, cx + 2.4, cy + 6], fill=colr)
    elif kind == "heli":
        d.ellipse([cx - 11, cy - 3, cx + 5, cy + 8], outline=colr, width=2)
        d.line([(cx - 16, cy - 8), (cx + 10, cy - 8)], fill=colr, width=2)
        d.line([(cx + 5, cy + 1), (cx + 14, cy - 4)], fill=colr, width=2)
        d.line([(cx + 14, cy - 8), (cx + 14, cy - 1)], fill=colr, width=2)
        d.line([(cx - 8, cy + 11), (cx + 4, cy + 11)], fill=colr, width=2)
    elif kind == "ballot":
        d.rectangle([cx - 12, cy + 1, cx + 12, cy + 12], outline=colr, width=2)
        d.rectangle([cx - 7, cy + 5, cx + 7, cy + 7], fill=colr)
        d.rectangle([cx - 5, cy - 12, cx + 5, cy + 2], outline=colr, width=2)
    elif kind == "chart":
        d.line([(cx - 12, cy + 12), (cx + 12, cy + 12)], fill=colr, width=2)
        d.line([(cx - 12, cy + 12), (cx - 12, cy - 12)], fill=colr, width=2)
        pts = [(cx - 10, cy + 7), (cx - 4, cy + 3), (cx + 1, cy + 5), (cx + 7, cy - 4),
               (cx + 12, cy - 9)]
        d.line(pts, fill=colr, width=2)
    elif kind == "drone":
        for dx, dy in [(-10, -10), (10, -10), (-10, 10), (10, 10)]:
            d.ellipse([cx + dx - 5, cy + dy - 2.4, cx + dx + 5, cy + dy + 2.4],
                      outline=colr, width=2)
            d.line([(cx, cy), (cx + dx, cy + dy)], fill=colr, width=2)
        d.rectangle([cx - 4, cy - 4, cx + 4, cy + 4], fill=colr)


CARDS = [
    dict(n=4, reg="EUROPE", topic="WAR", icon="burst", stat="2 DEAD", place="ODESA / KYIV",
         head="Strikes kill two in Odesa; drones over Kyiv",
         body="A Russian strike kills 2 and injures 3, including a child; drones set a Kyiv tower block ablaze."),
    dict(n=5, reg="AMERICAS", topic="SIEGE", icon="store", stat="10 FREED", place="CARTAGENA",
         head="Supermarket siege: gunmen hold shoppers",
         body="Gunmen flee a failed armoured-car raid into an Exito store, seizing 25 people; 10 freed, snipers ring the block."),
    dict(n=6, reg="ASIA", topic="LABOUR", icon="shirt", stat="+36%", place="DHAKA",
         head="Garment workers win a 36% pay rise",
         body="After weeks of protest and clashes in Gazipur, Bangladesh's garment workers win 36%; a 'double pay' demand fails."),
    dict(n=7, reg="AMERICAS", topic="CYBER", icon="lock", stat="BREACH", place="LANGLEY",
         head="CIA says unclassified system breached",
         body="A cyberattack breaches a CIA unclassified system; the agency says no classified data was compromised."),
    dict(n=8, reg="EUROPE", topic="DISASTER", icon="heli", stat="5 CREW", place="WESTERN TURKIYE",
         head="Army helicopter crash kills five crew",
         body="An AS-532 Cougar crashes on a training flight; all five crew die, the Defence Ministry says."),
    dict(n=9, reg="MIDDLE EAST", topic="POLITICS", icon="ballot", stat="28 SEATS", place="JERUSALEM",
         head="Eisenkot signs first coalition pact",
         body="Yashar agrees a deal with Lieberman's party - 28 seats together - in the race to form a government by 6 Dec."),
    dict(n=10, reg="AMERICAS", topic="ECONOMY", icon="chart", stat="103.3", place="WASHINGTON",
         head="Consumer confidence leaps to 103.3",
         body="US consumer confidence hits its highest in nearly two years on brighter views of jobs and the economy."),
    dict(n=11, reg="AFRICA", topic="WAR", icon="drone", stat="187", place="THE SAHEL",
         head="Insurgents take drone war to the skies",
         body="Reuters finds cheap drones reshaping West Africa's wars; JNIM alone logs 187 drone attacks since 2023."),
]

CARD_W = (CW - 48) // 4
CARD_H = 108
for idx, cd in enumerate(CARDS):
    cx0 = M + (idx % 4) * (CARD_W + 16)
    cy0 = CARDS_Y + (idx // 4) * (CARD_H + 10)
    colr = REG[cd["reg"]]
    d.rectangle([cx0, cy0, cx0 + CARD_W, cy0 + 3], fill=colr)
    badge(cx0 + 11, cy0 + 16, cd["n"], colr, r=9)
    d.text((cx0 + 25, cy0 + 9), f"{cd['reg']} - {cd['topic']}", font=F(SANS_B, 8.5), fill=GRAY)
    d.text((cx0 + 25, cy0 + 20), cd["place"], font=F(SANS_B, 8.5), fill=RED)
    icon(cd["icon"], cx0 + 20, cy0 + 52, colr)
    f_stat = fit(cd["stat"], SERIF_B, 14, 46, 10)
    d.text((cx0 + 20 - tw(cd["stat"], f_stat) / 2, cy0 + 68), cd["stat"], font=f_stat, fill=INK)
    tx = cx0 + 44
    f_ch = F(SANS_B, 11.5)
    hy = cy0 + 34
    for ln in wrap(cd["head"], f_ch, CARD_W - 48)[:2]:
        d.text((tx, hy), ln, font=f_ch, fill=INK)
        hy += 14
    f_cb = F(SANS, 9.3)
    for ln in wrap(cd["body"], f_cb, CARD_W - 48)[:3]:
        d.text((tx, hy + 1), ln, font=f_cb, fill=(52, 46, 38))
        hy += 11.5

BOT_Y = CARDS_Y + 2 * CARD_H + 10 + 14

# ---------------------------------------------------------------- world map
MAP_W = 396
d.rectangle([M, BOT_Y, M + MAP_W, BOT_Y + 20], fill=INK)
d.text((M + 8, BOT_Y + 5), "WHERE IT HAPPENED", font=F(SANS_B, 10), fill=(255, 255, 255))
sub = "pins carry the story numbers"
d.text((M + MAP_W - 8 - tw(sub, F(SERIF_I, 9.5)), BOT_Y + 5), sub, font=F(SERIF_I, 9.5),
       fill=(230, 220, 200))
MX, MY, MW, MH = M + 4, BOT_Y + 26, MAP_W - 8, 138
LAND = (216, 203, 168)
CONTINENTS = [
    [(0.02, 0.32), (0.06, 0.24), (0.12, 0.20), (0.19, 0.20), (0.24, 0.24), (0.265, 0.30),
     (0.25, 0.37), (0.275, 0.42), (0.25, 0.465), (0.215, 0.45), (0.205, 0.50), (0.16, 0.475),
     (0.10, 0.435), (0.045, 0.385)],
    [(0.225, 0.515), (0.285, 0.505), (0.325, 0.55), (0.325, 0.63), (0.30, 0.72), (0.275, 0.775),
     (0.255, 0.71), (0.235, 0.62), (0.215, 0.56)],
    [(0.44, 0.42), (0.52, 0.40), (0.565, 0.44), (0.555, 0.53), (0.575, 0.61), (0.54, 0.71),
     (0.495, 0.73), (0.465, 0.62), (0.45, 0.52)],
    [(0.435, 0.31), (0.475, 0.235), (0.54, 0.225), (0.575, 0.28), (0.55, 0.345), (0.50, 0.365), (0.455, 0.355)],
    [(0.575, 0.235), (0.66, 0.215), (0.76, 0.235), (0.845, 0.275), (0.865, 0.34), (0.80, 0.385),
     (0.775, 0.44), (0.715, 0.465), (0.695, 0.52), (0.66, 0.48), (0.635, 0.415), (0.60, 0.40), (0.58, 0.335)],
    [(0.79, 0.625), (0.875, 0.62), (0.895, 0.685), (0.85, 0.745), (0.795, 0.705)],
]
for poly in CONTINENTS:
    d.polygon([(MX + px * MW, MY + py * MH) for px, py in poly], fill=LAND)
for ex, ey in [(0.715, 0.555), (0.755, 0.575), (0.79, 0.56)]:
    d.ellipse([MX + ex * MW - 5, MY + ey * MH - 2.6, MX + ex * MW + 5, MY + ey * MH + 2.6], fill=LAND)

PINS = [(1, 0.698, 0.31), (2, 0.595, 0.42), (3, 0.222, 0.335), (4, 0.54, 0.295),
        (5, 0.24, 0.515), (6, 0.672, 0.425), (7, 0.243, 0.368), (8, 0.555, 0.335),
        (9, 0.578, 0.385), (10, 0.20, 0.365), (11, 0.472, 0.475), (17, 0.578, 0.25),
        (18, 0.72, 0.448), (20, 0.462, 0.35), (25, 0.508, 0.615), (26, 0.852, 0.715),
        (27, 0.752, 0.35)]
for num, px, py in PINS:
    cx, cy = MX + px * MW, MY + py * MH
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=RED, outline=(255, 255, 255), width=1)
    f_pin = F(SANS_B, 7.5)
    t = str(num)
    d.text((cx - tw(t, f_pin) / 2, cy - 4.8), t, font=f_pin, fill=(255, 255, 255))

# ---------------------------------------------------------------- briefs
BRIEFS = [
    (12, "Washington", "Trump pardons the Thanksgiving turkeys at the White House"),
    (13, "Washington", "Trump names prosecutor O'Neill to a federal judgeship"),
    (14, "Washington", "US sergeant admits selling military secrets to buyers in China"),
    (15, "New York", "Jury convicts Huawei of stealing trade secrets"),
    (16, "Washington", "Abrego Garcia to leave the US voluntarily, reports say"),
    (17, "Moscow", "Russia sends Chinese suspect in $2.3bn deposit case home"),
    (18, "Hong Kong", "Fire survivors return, a year after 168 died"),
    (19, "Geneva", "UN: HIV infections may rise from 2027 as funding falls"),
    (20, "Madrid", "Polls put People's Party first before Nov 29 snap vote"),
    (21, "Sacramento", "Extreme flooding threatens California"),
    (22, "Detroit", "Pentagon talks to GM, Ford on military drone output"),
    (23, "Tehran", "Iran rules out US talks until seven conditions are met"),
    (24, "London", "Report finds Met Police still institutionally racist"),
    (25, "Kinshasa", "Cobalt firms race to beat DR Congo export ban"),
    (26, "Canberra", "Australian inflation climbs more than expected"),
    (27, "Seoul", "Russian jets enter air defence zone, Seoul says"),
]
BX = M + MAP_W + 16
BW2 = W - M - BX
d.rectangle([BX, BOT_Y, W - M, BOT_Y + 20], fill=INK)
d.text((BX + 8, BOT_Y + 5), "ALSO ON WEDNESDAY 25 NOV", font=F(SANS_B, 10),
       fill=(255, 255, 255))
f_bn = F(SANS_B, 9.2)
f_bt = F(SANS, 9.2)
colw = (BW2 - 12) // 2
for ci in range(2):
    cx0 = BX + ci * (colw + 12)
    yy = BOT_Y + 27
    for num, place, text in BRIEFS[ci * 8:(ci + 1) * 8]:
        head = f"{num} {place} "
        d.text((cx0, yy), head, font=f_bn, fill=INK)
        rest = wrap(text, f_bt, colw - tw(head, f_bn))
        d.text((cx0 + tw(head, f_bn), yy), rest[0] if rest else "", font=f_bt, fill=(52, 46, 38))
        for ln in rest[1:2]:
            d.text((cx0 + 8, yy + 11), ln, font=f_bt, fill=(52, 46, 38))
        yy += 21 if len(rest) > 1 else 15.5

# ---------------------------------------------------------------- footer
hline(972, wdt=1)
f_dc = F(SANS, 9.3)
dc1 = ("DATE CHECK  Left out as other days' news - Tue 24 Nov: Landmine Monitor 2026 "
       "released in Geneva - Xinhua announces the Chen Jining probe - tankers catch fire "
       "in Hormuz. Mon 23 Nov: Nvidia rehires Huang.")
d.text((M, 978), dc1, font=fit(dc1, SANS, 9.3, CW, 7), fill=(70, 63, 52))
f_fin = F(SERIF_I, 9)
fin = ("Every story here happened on, or was first reported on, Wednesday 25 November 2026 "
       "in some time zone, as the named outlets reported it. Maps and drawings are original "
       "art made for this page.")
center(fin, 996, fit(fin, SERIF_I, 9, CW, 7), GRAY)
# red DATE CHECK label overlay
d.rectangle([M, 977, M + tw("DATE CHECK", F(SANS_B, 9.3)) + 2, 990], fill=PAPER)
d.text((M, 978), "DATE CHECK", font=F(SANS_B, 9.3), fill=RED)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(OUT, optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
