# Henry-gate

A **Henry-gate** a 2026-os magyar titkosszolgálati botrány nyilvános dokumentációja. Az ügy szereplői, időbeli szálai, a mozgatórugók és a felelősök köre jelenleg is vitatott és részben tisztázatlan — a feltárás folyamatban van.

Ez az oldal nem lezárt tényeket, hanem egy folyamatosan bővülő nyilvános idővonalat tartalmaz. Ha hibát találsz, vagy új forrással rendelkezel, hozzájárulhatsz a dokumentációhoz.
## Hogyan kontributálhatsz?
### Hibát találtál? — Nyiss egy Issue-t

Ha valamit tévesnek, hiányosnak vagy félrevezetőnek találsz (pl. helytelen dátum, rossz hivatkozás, pontatlan összefoglaló), nyiss egy [GitHub Issue-t](https://github.com/critic4lcode/henrygate/issues/new).

Az Issue-ban tüntesd fel:
- melyik eseményről van szó (dátum vagy cím)
- mi a pontatlanság
- mi lenne a helyes adat — **forrással együtt** (lásd lent)

### Új forrást vagy eseményt szeretnél hozzáadni? — Küldj Pull Requestet
Minden új tartalom egy `.md` fájl a `content/` mappában, a következő névformátumban:

```
YYYY-MM-DD-rovid-cim.md
```

Kötelező frontmatter a fájl elején:

```markdown
---
date: "YYYY-MM-DD"
title: "Az esemény rövid címe"
tags: [henry-gate, gundalf, nni, ...]
---
```
Ha az időszak nem bizonyos (év vagy hónap pontosság áll csak rendelkezésre), akkor ??-t használj számok helyett:
```markdown
---
date: "2020-??-??" -> 2020 környékén
date: "2026-03-??" -> 2026 március környékén
---
```

## Forrásmegjelölési szabályok
**Minden kijelentéshez forrást kell rendelni.** Forrás nélküli állítások nem kerülnek be az idővonalra. _(A hiányos források pótlása folyamatban van)_

### Elfogadott formátumok
**YouTube videó — timestampelt hivatkozás kötelező, ha konkrét állításra mutatsz:**
```
[YYYY-MM-DD:  Videó cím (Csatornanév, YouTube)](https://www.youtube.com/watch?v=VIDEOID&t=1234)
```

**Írott cikk:**
```
[YYYY-MM-DD: Cikk címe (Média neve)](https://...)
```

### Ami nem elfogadható forrásként
- Névtelen vagy ellenőrizhetetlen forrás
- Forrás nélküli „köztudott" állítások

## Stílusbeli elvárások

- Tárgyilagos, kommentár nélküli hangnem
- Az eseményeket úgy írd le, ahogy a forrásban szerepelnek
- Ha egy állítás vitatott: „X szerint..." vagy „Y tagadja, hogy..."
- Kerüld az érzelmi töltetű szavakat és minősítéseket

## Kapcsolat

[sssh38@proton.me](mailto:sssh38@proton.me)
