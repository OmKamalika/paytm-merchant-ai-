# Paytm Brand Design Guide

A practical design reference for building Paytm-themed interfaces (for example, the Paytm Merchant AI experience).

> **Accuracy note (please read).** Paytm does not publish a complete public brand specification. The values below are assembled from Paytm's logo, public web and app UI, and common usage.
> - Values marked ✅ are widely documented and stable (the two logo colours).
> - Values marked 🔶 are **recommended design tokens** that match the look of Paytm's product UI. They are not an official spec.
> - Before shipping externally, confirm the final values with Paytm's brand team or by sampling their current app and website.
> - Paytm's UI typeface is proprietary. The guide gives a free, licensable fallback stack.

---

## 1. Brand Ideology

### 1.1 Essence
Paytm began as "Pay Through Mobile" and grew into India's largest consumer-fintech super-app. The brand promise is **making digital finance simple, trustworthy and available to everyone**, from first-time smartphone users to large merchants.

### 1.2 Core values

| Value | What it means | How it shows up in design |
|---|---|---|
| **Trust** | Money is serious. Users must feel safe. | Deep navy, generous white space, clear confirmations, no visual noise around payments |
| **Simplicity** | Anyone should be able to pay in seconds. | One primary action per screen, plain language, large tap targets |
| **Inclusion** | Built for India: first-time users, regional languages, low-end devices. | High contrast, legible type sizes, icon plus label, lightweight screens |
| **Speed & energy** | Instant payments, a modern attitude. | Bright cyan accent, quick micro-interactions, crisp transitions |
| **Empowerment (merchants)** | Tools that help small businesses grow. | Dashboard clarity, positive-reinforcement green, plain-language insights |

### 1.3 Personality and tone of voice
- **Friendly, not casual.** Warm and direct, never slangy around money.
- **Clear, not clever.** "Payment successful", not "Boom! Money moved!".
- **Reassuring in errors.** Say what happened, whether money is safe, and what to do next.
- **Bilingual-ready.** Short strings that survive translation into Hindi and other Indian languages. Avoid idioms.

### 1.4 Visual principles
1. **Blue is the brand, navy is the trust.** Cyan signals action and energy. Navy signals seriousness and structure.
2. **White is the canvas.** Content sits on clean white or very light grey surfaces.
3. **One hero action per view.** The primary button is always the most saturated element on screen.
4. **Colour carries meaning.** Green means success or received, red means failure or alert, amber means pending. Never use these decoratively.
5. **Rounded and approachable.** Soft corners, friendly icons, no sharp ornamentation.

---

## 2. Colour System

### 2.1 Brand colours (primary and secondary)

| Role | Name | Hex | RGB | Status |
|---|---|---|---|---|
| **Primary** | Paytm Blue (cyan) | `#00BAF2` | 0, 186, 242 | ✅ Logo colour |
| **Secondary** | Paytm Navy | `#002E6E` | 0, 46, 110 | ✅ Logo colour |
| **Tertiary / accent** | Sky Tint | `#E5F7FD` | 229, 247, 253 | 🔶 |

> Some Paytm assets use `#012B72` for navy and `#00B9F5` for the blue. These are visually indistinguishable from the values above. Pick one set and use it consistently.

### 2.2 Background colours

The three tiers requested: primary, secondary and tertiary backgrounds.

| Tier | Token | Hex | Use | Status |
|---|---|---|---|---|
| **Primary background** | `--bg-primary` | `#FFFFFF` | App canvas, cards, sheets, modals, inputs | ✅ |
| **Secondary background** | `--bg-secondary` | `#F5F7FA` | Page backdrop behind white cards, list zebra, disabled fields | 🔶 |
| **Tertiary background** | `--bg-tertiary` | `#E5F7FD` | Highlight panels, info banners, selected rows, soft brand tint | 🔶 |
| **Brand surface (dark)** | `--bg-brand` | `#002E6E` | Headers, hero bands, dark-mode base, footers | ✅ |
| **Brand surface (bright)** | `--bg-accent` | `#00BAF2` | Primary buttons, active tab indicators, promo strips | ✅ |

### 2.3 Text colours

| Token | Hex | Use | Contrast on white |
|---|---|---|---|
| `--text-primary` | `#1D2D3E` | Headings and body | ≈ 14:1 (AAA) |
| `--text-secondary` | `#506D85` | Captions, helper text, labels | ≈ 5.3:1 (AA) |
| `--text-disabled` | `#9AA9B8` | Disabled content | Decorative only |
| `--text-on-brand` | `#FFFFFF` | Text on navy and on cyan buttons | Navy ≈ 13:1. **Cyan ≈ 2.4:1, so use bold navy text on cyan for small text** |
| `--text-link` | `#00BAF2` on dark, `#0086B8` on light | Links | `#0086B8` ≈ 4.0:1, so use it for large or bold text only |

> **Accessibility caution:** white text on `#00BAF2` fails WCAG AA for body-size text. For cyan buttons, use either large and bold white text (18px and above, or 14px bold and above) or navy `#002E6E` text.

### 2.4 Semantic colours (🔶 recommended)

| Meaning | Hex | Tint (backgrounds) |
|---|---|---|
| Success / money received | `#21C17C` | `#E6F8F0` |
| Error / failed / alert | `#FD5C5C` | `#FFECEC` |
| Warning / pending | `#FFB020` | `#FFF4DB` |
| Info | `#00BAF2` | `#E5F7FD` |

### 2.5 Borders and dividers
- Default border: `#E0E6ED`
- Subtle divider: `#EEF2F6`
- Focus ring: 2px `#00BAF2` with 2px offset

### 2.6 Proportion guide (60 / 30 / 10)
- **60%** white and light-grey surfaces
- **30%** navy for text, headers and structure
- **10%** cyan for actions and highlights

### 2.7 CSS tokens

```css
:root {
  /* Brand */
  --paytm-blue: #00BAF2;
  --paytm-navy: #002E6E;
  --paytm-sky:  #E5F7FD;

  /* Backgrounds */
  --bg-primary:   #FFFFFF;
  --bg-secondary: #F5F7FA;
  --bg-tertiary:  #E5F7FD;
  --bg-brand:     #002E6E;
  --bg-accent:    #00BAF2;

  /* Text */
  --text-primary:   #1D2D3E;
  --text-secondary: #506D85;
  --text-disabled:  #9AA9B8;
  --text-on-brand:  #FFFFFF;
  --text-link:      #0086B8;

  /* Semantic */
  --success: #21C17C;  --success-bg: #E6F8F0;
  --error:   #FD5C5C;  --error-bg:   #FFECEC;
  --warning: #FFB020;  --warning-bg: #FFF4DB;

  /* Lines */
  --border:  #E0E6ED;
  --divider: #EEF2F6;
}
```

### 2.8 Dark mode (🔶)

| Token | Hex |
|---|---|
| Primary background | `#0B1A33` |
| Secondary background (cards) | `#12264A` |
| Tertiary background (highlight) | `#1B3563` |
| Text primary | `#FFFFFF` |
| Text secondary | `#A9B8CE` |
| Accent | `#00BAF2` (unchanged) |

---

## 3. Typography

### 3.1 Typeface
Paytm's product UI uses a clean, geometric, humanist sans-serif (a proprietary **"Paytm Sans"** face in its newer apps). It is not publicly licensed, so use the stack below.

| Priority | Font | Why |
|---|---|---|
| 1 | **Paytm Sans** | Only if you hold a licence from Paytm |
| 2 | **Inter** | Free, very close in proportions, excellent number rendering |
| 3 | **Roboto** | Native Android feel, familiar to Indian users |
| 4 | System fallback | `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif` |

```css
font-family: "Paytm Sans", "Inter", "Roboto", -apple-system, "Segoe UI",
             Helvetica, Arial, sans-serif;
```

For Indian-language text, pair with **Noto Sans Devanagari**, **Noto Sans Tamil** and similar. Increase line-height by about 10% for Indic scripts.

Enable tabular figures for amounts so digits align: `font-variant-numeric: tabular-nums;`

### 3.2 Weights

| Weight | Value | Use |
|---|---|---|
| Regular | 400 | Body text, descriptions |
| Medium | 500 | Labels, list titles, navigation |
| Semibold | 600 | Buttons, section headings, amounts |
| Bold | 700 | Page titles, hero numbers |

Avoid weights below 400. Avoid 800 and above, which looks heavy and un-Paytm-like.

### 3.3 Type scale (🔶 mobile first)

| Style | Size / line-height | Weight | Letter-spacing | Use |
|---|---|---|---|---|
| Display | 32 / 40 px | 700 | -0.5px | Hero balance, large amounts |
| H1 | 24 / 32 px | 700 | -0.25px | Screen titles |
| H2 | 20 / 28 px | 600 | 0 | Section headings |
| H3 | 18 / 24 px | 600 | 0 | Card titles |
| Body L | 16 / 24 px | 400 | 0 | Primary reading text |
| Body M | 14 / 20 px | 400 | 0 | Default UI text, lists |
| Label | 14 / 20 px | 500 | 0.1px | Form labels, tabs |
| Button | 16 / 24 px | 600 | 0.2px | Buttons |
| Caption | 12 / 16 px | 400 | 0.2px | Helper text, timestamps |
| Overline | 11 / 16 px | 600 | 0.8px (uppercase) | Category tags |

**Minimum sizes:** body 14px, caption 12px. Never go below 11px.

### 3.4 Desktop and web scaling

| Style | Mobile | Desktop |
|---|---|---|
| Display | 32 | 48 |
| H1 | 24 | 36 |
| H2 | 20 | 28 |
| Body | 14 to 16 | 16 |

---

## 4. Layout, Shape and Elevation

### 4.1 Spacing (4px base grid)
`4 · 8 · 12 · 16 · 20 · 24 · 32 · 48 · 64`

- Screen side padding: **16px** on mobile, **24px** on tablet, content max-width **1200px** on desktop.
- Card inner padding: **16px**.
- Gap between stacked cards: **12px**.

### 4.2 Corner radius

| Element | Radius |
|---|---|
| Buttons | 8px (or fully pill, 999px, for hero CTAs) |
| Inputs | 8px |
| Cards | 12px |
| Bottom sheets and modals | 16px top corners |
| Chips and tags | 999px |
| Avatars and icons in circles | 50% |

### 4.3 Elevation

| Level | Shadow | Use |
|---|---|---|
| 0 | none, 1px `#E0E6ED` border | Flat list items |
| 1 | `0 1px 4px rgba(16,40,80,0.08)` | Cards |
| 2 | `0 4px 16px rgba(16,40,80,0.12)` | Sticky headers, popovers |
| 3 | `0 8px 32px rgba(16,40,80,0.16)` | Modals and bottom sheets |

Shadows are tinted with navy, never pure black.

---

## 5. Components

### 5.1 Buttons

| Variant | Background | Text | Border | Notes |
|---|---|---|---|---|
| **Primary** | `#00BAF2` | `#002E6E` (or large bold white) | none | One per screen |
| **Primary (dark)** | `#002E6E` | `#FFFFFF` | none | On light surfaces for high-trust actions |
| **Secondary** | `#FFFFFF` | `#002E6E` | 1.5px `#002E6E` | Alternative action |
| **Tertiary / text** | transparent | `#0086B8` | none | Low emphasis |
| **Destructive** | `#FD5C5C` | `#FFFFFF` | none | Cancel, delete |
| **Disabled** | `#E0E6ED` | `#9AA9B8` | none | |

- Height: **48px** (touch), **40px** compact. Minimum width 88px.
- States: hover darkens 8%, pressed darkens 14%, focus shows the 2px cyan ring.

### 5.2 Inputs
- Height 48px, radius 8px, border 1px `#E0E6ED`, background `#FFFFFF`.
- Focus: border `#00BAF2` plus 2px outer glow `rgba(0,186,242,0.25)`.
- Error: border `#FD5C5C` with helper text in the same colour.
- Label above the field (Label style), helper text below (Caption).

### 5.3 Cards
White background, 12px radius, elevation 1, 16px padding. Merchant KPI cards use Display type for the figure and Caption for the delta, with green or red for the trend.

### 5.4 Navigation
- Top app bar: navy `#002E6E` with white text, or white with navy text. Height 56px.
- Bottom tab bar: white, 56 to 64px, active icon and label in `#00BAF2`, inactive in `#506D85`.

### 5.5 Iconography
- Outlined, 2px stroke, rounded caps, 24px grid.
- Navy or cyan only. Semantic colours only for status icons.
- Always pair with a text label for primary navigation.

### 5.6 Motion
- Duration: 150 to 250ms for UI, up to 400ms for sheets.
- Easing: `cubic-bezier(0.2, 0, 0, 1)`.
- Payment success: a short check animation in `#21C17C`. Keep it under one second.
- Respect `prefers-reduced-motion`.

---

## 6. Merchant AI Application Notes

Guidance for this repository's merchant-facing AI features:

1. **Dashboard header:** navy `#002E6E` band with white text, followed by white cards on a `#F5F7FA` backdrop.
2. **AI insight panels:** use the tertiary background `#E5F7FD` with a 4px left border in `#00BAF2`, so AI-generated suggestions look clearly different from hard transactional data.
3. **Chat bubbles:** user messages in `#00BAF2` with navy text, assistant messages in `#FFFFFF` with a 1px border and `#1D2D3E` text.
4. **Numbers first:** show amounts in Display or H1 with tabular figures and the ₹ symbol, using the Indian digit grouping (`₹1,25,000`).
5. **Always explain AI output** in plain language, and give a clear way to act on it (one primary cyan button).
6. **Safe-money messaging:** on any error, state clearly whether funds were debited.
7. **Language:** build for English and Hindi from day one, and leave about 30% extra space in components for longer translated strings.

---

## 7. Do and Don't

| Do | Don't |
|---|---|
| Use white as the dominant surface | Fill whole screens with cyan |
| Keep one cyan primary action per screen | Place several cyan buttons side by side |
| Pair cyan with navy text for small labels | Use white text on cyan below 18px |
| Use green and red strictly for status | Use green or red as decoration |
| Use navy-tinted shadows | Use harsh black shadows |
| Show amounts in tabular figures | Mix proportional digits in tables |
| Alter the logo only per Paytm's brand rules | Recolour, stretch or add effects to the logo |

---

## 8. Quick Reference

```
PRIMARY BLUE   #00BAF2    secondary NAVY   #002E6E    tertiary SKY   #E5F7FD
BG primary     #FFFFFF    BG secondary     #F5F7FA    BG tertiary    #E5F7FD
TEXT primary   #1D2D3E    TEXT secondary   #506D85
SUCCESS        #21C17C    ERROR            #FD5C5C    WARNING        #FFB020

FONT   Paytm Sans > Inter > Roboto > system sans
WEIGHT 400 body · 500 label · 600 button/heading · 700 title
SIZE   32 display · 24 h1 · 20 h2 · 16 body-l · 14 body · 12 caption
RADIUS 8 buttons/inputs · 12 cards · 16 sheets
GRID   4px base, 16px screen padding
```

---

*Logo usage, official asset files and legal brand rules belong to Paytm (One97 Communications Ltd.). Use this guide for UI styling and obtain brand assets directly from Paytm.*
