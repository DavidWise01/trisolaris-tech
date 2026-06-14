#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build TRISOLARIS · THE TECHNOLOGIA (3BT) — a HUB-AND-SPOKE dissection of the technology across all three
media of the Three-Body universe (books + Tencent 2023 + Netflix 2024). The HUB catalogs 12 technologies with
3-media presence chips and an honest real-science verdict each; SIX of them get their own dedicated SPOKE
repos (full single-tech dissection pages + .dlw). Companion to [[three-body-pocket-universe]] (3BP).
Themed engineering-blueprint (cyan schematic on black). One generator builds the hub AND all 6 spokes.
Facts inherited from the dual-agent verification done for 3BP; science verdicts apply the honest-fluff
discipline. Spokes: sophon · the-droplet · dual-vector-foil · red-coast · nanofilament · curvature-drive."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

HUB_AX = "3BT"
GH = "https://davidwise01.github.io"

# ── verdict + media palettes ──
VCOL = {"REAL":"#57c79a","SPECULATIVE":"#f5b942","HALF":"#6fb0e8","FLUFF":"#ff5a4d"}
MEDIA = {"books":("📖 BOOKS","#f5b942"),"tencent":("TENCENT ’23","#57c79a"),"netflix":("NETFLIX ’24","#6fb0e8")}

# ── glyphs (small schematic SVGs per tech) ──
def g_sophon():
    return ('<g fill="none" stroke="#2ce0e0" stroke-width="1.4">'
            '<circle cx="40" cy="40" r="9"/>'
            '<rect x="58" y="20" width="40" height="40"/>'
            +"".join(f'<line x1="58" y1="{24+i*6}" x2="98" y2="{24+i*6}" stroke-width="0.6"/>' for i in range(6))
            +'<path d="M49 40 Q56 28 58 30" stroke-dasharray="3 3"/></g>')
def g_droplet():
    return ('<g><path d="M70 12 C70 12 96 50 96 64 a26 26 0 1 1 -52 0 C44 50 70 12 70 12 Z" fill="none" stroke="#2ce0e0" stroke-width="1.4"/>'
            '<ellipse cx="60" cy="58" rx="6" ry="10" fill="#eafcff" opacity="0.5"/></g>')
def g_dvf():
    return ('<g fill="none" stroke="#2ce0e0" stroke-width="1.3">'
            '<path d="M30 30 L70 30 L82 18 M30 30 L30 62 L42 50 M70 30 L70 62 M30 62 L70 62 L82 50 L82 18 M42 50 L82 50 M42 18 L42 50 M42 18 L82 18"/>'
            '<line x1="20" y1="78" x2="110" y2="78" stroke="#ff5a4d" stroke-width="2"/></g>')
def g_redcoast():
    return ('<g fill="none" stroke="#2ce0e0" stroke-width="1.4">'
            '<path d="M40 70 A34 34 0 0 1 92 44" /><line x1="66" y1="56" x2="66" y2="82"/><line x1="52" y1="82" x2="80" y2="82"/>'
            '<g stroke="#f5b942" stroke-width="1"><path d="M84 30 q10 6 6 18" stroke-dasharray="2 3"/><path d="M90 22 q16 9 9 30" stroke-dasharray="2 3"/></g></g>')
def g_nano():
    return ('<g><rect x="26" y="40" width="68" height="22" rx="3" fill="none" stroke="#2ce0e0" stroke-width="1.4"/>'
            '<g stroke="#ff5a4d" stroke-width="1">'+"".join(f'<line x1="{30+i*16}" y1="18" x2="{30+i*16}" y2="84"/>' for i in range(5))+'</g></g>')
def g_curv():
    return ('<g fill="none" stroke="#2ce0e0" stroke-width="0.9">'
            +"".join(f'<path d="M16 {24+i*10} Q60 {24+i*10+(0 if i<2 else 0)} 60 {44} Q60 {44} 104 {24+i*10}"/>' for i in range(6))
            +'<ellipse cx="60" cy="44" rx="16" ry="22" stroke="#f5b942" stroke-width="1.3"/></g>')
GLYPH = {"sophon":g_sophon,"the-droplet":g_droplet,"dual-vector-foil":g_dvf,"red-coast":g_redcoast,"nanofilament":g_nano,"curvature-drive":g_curv}

# ── the 12 technologies ──
# fields: slug, ax, name, cn, cat, media[], verdict, tagline, what, across, science, oneline, repo(bool)
T = lambda **k: k
TECH = [
 T(slug="red-coast", ax="RDC", name="Red Coast", cn="红岸", cat="CONTACT & SURVEILLANCE",
   media=["books","tencent","netflix"], verdict="HALF", repo=True,
   tagline="the antenna that answered — solar-amplified radio first contact",
   what="The secret Cold-War-era installation where Ye Wenjie discovers she can use the Sun as an amplifier to boost a radio transmission to interstellar power, and sends humanity's first reply to Trisolaris — the single act from which the whole saga flows.",
   across="The Red Coast dish, the Cultural-Revolution backstory, and Ye Wenjie's fateful broadcast are present in all three media — the books, Tencent's faithful Chinese series, and Netflix's relocated version (which keeps the Cultural-Revolution prologue and the young Ye Wenjie intact).",
   science="HALF. Radio SETI is entirely real (Arecibo, the 1974 Arecibo Message), and the danger of broadcasting our location — the METI debate — is a live, serious argument among scientists. The dramatized part is the trick: using the Sun's plasma as a giant radio amplifier to reach four light-years is physically dubious as written. Real contact tech, fictional amplifier.",
   oneline="One woman, one dish, one Sun for an amplifier — and the silence of Earth was over forever."),
 T(slug="sophon", ax="SPH", name="The Sophon", cn="智子", cat="CONTACT & SURVEILLANCE",
   media=["books","tencent","netflix"], verdict="FLUFF", repo=True,
   tagline="a proton unfolded into a computer — the leash on human science",
   what="The Trisolarans take a single proton, unfold its higher-dimensional micro-structure into a 2D sheet large enough to wrap a planet, etch a sentient supercomputer onto it, then refold it to subatomic size. Sent to Earth at near-light speed, the sophons jam humanity's particle-accelerator results (so we can never out-tech Trisolaris before the fleet arrives), surveil everything, and report home instantly.",
   across="The sophons, the 'physics has stopped working' crisis, and the eerie countdown drive the mystery of book one — and appear across all three media (the Tencent series and Netflix both dramatize the broken experiments and the sophon reveal).",
   science="FLUFF — clever, but fiction. A proton is not a multi-dimensional object you can unfold and etch circuits onto; the source-faithful figure is NINE micro-dimensions (often misquoted as 11). And the instant link home is impossible: quantum entanglement cannot carry information faster than light (the no-communication theorem). Imaginative pseudoscience dressed in real terminology.",
   oneline="One proton, unfolded and inscribed: it froze your physics and read your every word — though the instant link home was always more wish than physics."),
 T(slug="the-droplet", ax="DRP", name="The Droplet", cn="水滴", cat="WEAPONS",
   media=["books","netflix"], verdict="FLUFF", repo=True,
   tagline="a perfect mirror that kills — the strong-force probe",
   what="A small (~3.5 m) teardrop Trisolaran probe whose hull is made of 'strong-interaction-force material' — giving it a perfectly mirror-smooth, near-absolute-zero, indestructible surface. In the Doomsday Battle it rams straight through Earth's combined space fleet, destroying roughly two thousand warships in minutes.",
   across="The Droplet's annihilation of the fleet is a book-two set-piece; Netflix brings it forward into season one. (Tencent's 2023 series adapts book one only, so its full battle is still to come there.)",
   science="FLUFF. The strong nuclear force acts only at femtometre range — you cannot build a macroscopic hull out of it. A flawless, frictionless, indestructible mirror is fantasy. The honest nod: ultra-dense degenerate matter (white-dwarf / neutron-star material) is real, and unimaginably strong — but it is not a teardrop you can fly through a fleet.",
   oneline="They saw me approach and called me a gift. I went through their two thousand ships like a needle through smoke."),
 T(slug="dual-vector-foil", ax="DVF", name="The Dual-Vector Foil", cn="二向箔", cat="WEAPONS",
   media=["books"], verdict="FLUFF", repo=True,
   tagline="death by art — collapsing 3D space into 2D",
   what="A dark-forest weapon: a small slip of material that initiates a runaway collapse of three-dimensional space into two dimensions. An unknown civilization flicks one into the Solar System, flattening the Sun and planets into a beautiful, lethal plane — the casual execution of a star system as a work of art.",
   across="The dual-vector foil and the two-dimensionalization of the Solar System are the climax of Death's End — book three only. Neither live-action series has reached it yet, which makes it the purest 'on the page' marvel of the universe.",
   science="FLUFF — and gorgeous. There is no known mechanism to lower a region of space out of a dimension. It rhymes loosely with real speculative ideas (extra spatial dimensions in string theory; false-vacuum decay as a cosmic phase change), but as written it is pure science fiction. Distinct from the photoid — that one is a kinetic star-killer; this one is a change to the rules of space itself.",
   oneline="I am not a bomb. I am a lowering — I fold your three dimensions down to two and turn your whole world into a painting of itself."),
 T(slug="nanofilament", ax="NNF", name="The Nanofilament “Flying Blade”", cn="飞刃", cat="MATERIALS & COMPUTATION",
   media=["books","tencent","netflix"], verdict="SPECULATIVE", repo=True,
   tagline="the molecular wire that sliced a ship — and the one device in all three media",
   what="Wang Miao's research material: an ultra-strong molecular filament, finer than a hair and stronger than anything known. In the 'Guzheng' (zither) operation, dozens of these wires are strung across a canal to slice the ETO's ship Judgment Day — and everyone aboard — cleanly into ribbons as it passes, to recover the data inside.",
   across="The flying-blade / ship-slicing operation is one of the few set-pieces that appears in ALL THREE media — book one, Tencent's series, and Netflix's (relocated, but the wires-across-the-waterway sequence is kept). The signature 'in all three' technology of the universe.",
   science="SPECULATIVE — closest to real. Super-strong nanomaterials are a genuine, active field: carbon nanotubes and graphene have extraordinary tensile strength, and 'monofilament that cuts anything' extrapolates from real research. The exaggeration is the feat (slicing a steel ship and its crew like soft cheese, with invisible wires), not the premise. The realest weapon in the saga.",
   oneline="Finer than a hair, stronger than steel — string enough of me across the water and a ship sails through into ribbons."),
 T(slug="curvature-drive", ax="CRV", name="Curvature Propulsion", cn="曲率驱动", cat="PROPULSION & STRUCTURES",
   media=["books"], verdict="SPECULATIVE", repo=True,
   tagline="lightspeed by bending spacetime — and the black domain",
   what="Humanity's (and others') endgame propulsion: ships that reach lightspeed not by accelerating through space but by warping spacetime itself, leaving a tell-tale trail. Related: the 'black domain,' a region where the speed of light is lowered to make a civilization slow, dark, and safe — a place to hide from the dark forest.",
   across="Curvature drive, lightspeed ships, and the black domain are late-trilogy (Death's End) concepts — books only so far; the live-action series have not reached them.",
   science="SPECULATIVE — with real math underneath. The Alcubierre drive (1994) is a genuine general-relativity solution that achieves effective faster-than-light travel by contracting space ahead and expanding it behind — but it requires vast amounts of negative-energy 'exotic matter' no one knows how to make. The black domain (locally slowing light as a hideout) is pure fiction. Real warp metric, fictional everything else.",
   oneline="I don't move you through space. I bend the space — and leave a wake that tells the dark forest exactly where you went."),
 # ── catalogued in the hub only (no dedicated repo) ──
 T(slug="human-computer", ax=None, name="The Human-Formation Computer", cn="人列计算机", cat="MATERIALS & COMPUTATION",
   media=["books","tencent","netflix"], verdict="REAL", repo=False,
   tagline="thirty million soldiers as a CPU — inside the Three-Body game",
   what="Inside the Three-Body VR game, an emperor builds a working computer out of thirty million soldiers holding signal flags — gates, registers, a bus — to compute the motion of the three suns. A dramatization of von Neumann architecture made of people.",
   across="The game and its human computer appear across all three media (the VR sequences in both series).",
   science="REAL (concept), dramatized scale. Computation is substrate-independent: you genuinely can build logic gates — and therefore a computer — out of people with flags, dominoes, water, or Minecraft redstone. The most scientifically honest idea in the whole universe; only the scale is theatrical.",
   oneline="A computer doesn't need silicon. Give thirty million people flags and a rulebook, and they will think."),
 T(slug="the-staircase", ax=None, name="The Staircase Program", cn="阶梯计划", cat="PROPULSION & STRUCTURES",
   media=["books","netflix"], verdict="SPECULATIVE", repo=False,
   tagline="a radiation sail pushed by nuclear bombs — to launch a brain at the stars",
   what="To get a spy to the Trisolaran fleet, humanity launches a tiny payload — in the end, only a frozen human brain (Yun Tianming's) — on a sail accelerated by a chain of detonating nuclear bombs to a fraction of lightspeed.",
   across="The Staircase Program (Will Downing's arc) is book three; Netflix brings it into season one. Tencent has not reached it.",
   science="SPECULATIVE — grounded. Light/radiation sails are real (IKAROS 2010, LightSail 2; Breakthrough Starshot's laser-sail plan), and nuclear-pulse propulsion (Project Orion) is real engineering. Pushing a sail to ~1% of light is a serious extrapolation. The dubious part is the brain-only payload surviving and being usable.",
   oneline="We could not send a person to the stars. So we sent a brain, on a sail, pushed by bombs."),
 T(slug="space-elevator", ax=None, name="The Space Elevator", cn="太空电梯", cat="PROPULSION & STRUCTURES",
   media=["books"], verdict="REAL", repo=False,
   tagline="a ribbon to orbit — the megastructure that's only waiting on materials",
   what="In the post-deterrence era humanity builds space elevators — tethers from the ground to geostationary orbit — to lift people and cargo cheaply off Earth.",
   across="A book-three fixture; not reached by the live-action series.",
   science="REAL (concept), pending materials. The space elevator is a seriously-studied megastructure (Tsiolkovsky proposed it in 1895). The only blocker is tether strength: it needs a flawless ribbon of something like carbon nanotube or graphene. Physics says yes; materials science says not yet.",
   oneline="No rockets. Just a ribbon to the sky strong enough not to snap under its own weight — the one piece we don't have."),
 T(slug="hibernation", ax=None, name="Hibernation", cn="冬眠", cat="MIND & SURVIVAL",
   media=["books","netflix"], verdict="SPECULATIVE", repo=False,
   tagline="cryosleep across centuries — how the cast survives the long war",
   what="Medical hibernation lets characters (Luo Ji, Cheng Xin, Da Shi) sleep across the centuries between crises, so a few human beings can witness the whole four-hundred-year arc.",
   across="A pervasive device in books two and three; Netflix uses it to carry its cast forward.",
   science="SPECULATIVE. Real medicine has therapeutic hypothermia and active research into induced torpor (NASA has funded torpor studies for Mars crews), but true long-duration, reversible human hibernation is unproven, and cryonics (freezing the dead) is not reversible today. Plausible direction, not yet real.",
   oneline="The war was four centuries long. So a few of us learned to sleep through the parts in between."),
 T(slug="deterrence-broadcast", ax=None, name="Deterrence Broadcast & the Photoid", cn="引力波广播 · 光粒", cat="WEAPONS",
   media=["books"], verdict="HALF", repo=False,
   tagline="gravitational-wave antennas that hold a world hostage — and the star-killing bullet",
   what="Dark-forest deterrence is enforced by gravitational-wave transmitters that can broadcast Trisolaris's coordinates to the silent hunters. The proof that the dark forest is real: a 'photoid,' a near-lightspeed kinetic projectile, is used to destroy a star (187J3X1).",
   across="Both are book-two/three concepts; not reached by the live-action series.",
   science="HALF. Gravitational waves are completely real — LIGO detected them in 2015 (Nobel 2017). But using them as a galaxy-wide, directional communications beacon is fiction: they are absurdly hard to generate or detect at any usable signal level. The photoid (a light-speed star-killing bullet) is FLUFF.",
   oneline="Gravitational waves are real; using them to whisper your enemy's address to the hunters is not."),
 T(slug="mental-seal", ax=None, name="The Mental Seal & the Wallfacers", cn="思想钢印 · 面壁者", cat="MIND & SURVIVAL",
   media=["books","netflix"], verdict="FLUFF", repo=False,
   tagline="strategy hidden in the mind — and a machine that installs belief",
   what="Because sophons read everything but human thought, the Wallfacers plan in secret inside their own minds. One Wallfacer, the neuroscientist Bill Hines, builds the 'mental seal' — a device that can stamp an unshakable belief directly into a brain.",
   across="The Wallfacer Project and the mental seal are book two; Netflix carries the Wallfacer idea through Saul Durand.",
   science="FLUFF (the seal); thought-experiment (the Wallfacers). There is no device that installs a specific, unshakable proposition into a brain by neural manipulation — belief and brainwashing are not clean switches. The Wallfacer concept itself is a sharp thought experiment about the one thing that can't be surveilled: intention.",
   oneline="They could read every word we wrote — so we hid the war behind the only wall left: the inside of a human skull."),
]
CATS = ["CONTACT & SURVEILLANCE","WEAPONS","PROPULSION & STRUCTURES","MATERIALS & COMPUTATION","MIND & SURVIVAL"]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f"{slug}.attribute"),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f"{slug}.agent"),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f"{slug}.spun"),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",HUB_AX)))
    open(os.path.join(out_dir,f"{slug}.moniker"),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",HUB_AX)))
    open(os.path.join(out_dir,f"{slug}.1099"),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",HUB_AX)))
    open(os.path.join(out_dir,f"{slug}.carbon.tiff"),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f"{slug}.silicon.png"),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok)}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")
def tech_rec(t):
    return {"name":t["name"],"axiom":t.get("ax") or HUB_AX,"emergence":"electrical","seal":t["oneline"],
            "origin":"3BT · The Technologia of Trisolaris","position":t["tagline"],"role":t["tagline"],
            "nature":t["what"],"mechanism":t["science"],"crystallization":t["across"],"witness":t["oneline"],
            "conductor":"ROOT0 (catalogued into UD0)","inputs":"Remembrance of Earth's Past + adaptations; real-science verdict","source":"The Three-Body Problem tech, catalogued by ROOT0"}

# ───────────────────────── shared CSS (engineering blueprint) ─────────────────────────
CSS = """*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
:root{--ink:#05070c;--ink2:#0b0f18;--ink3:#10141f;--pa:#dfeaf2;--pa2:#8fa3b8;--acc:#2ce0e0;--gold:#f5b942;--red:#ff5a4d;--green:#57c79a;--blue:#6fb0e8;
--dim:#566273;--line:#18222e;--faint:#0e141d;--disp:"Chakra Petch",sans-serif;--head:"Space Mono",monospace;--body:"Rajdhani",system-ui,sans-serif;--mono:"Space Mono",monospace;}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden;font-size:17px}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:linear-gradient(rgba(44,224,224,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(44,224,224,.025) 1px,transparent 1px);background-size:32px 32px}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:32px 0 26px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--acc)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 22px;background:#05070c;box-shadow:0 0 20px rgba(44,224,224,.08)}
.egg{cursor:help;transition:filter .5s}.egg:hover{filter:drop-shadow(0 0 10px #2ce0e0)}
h1{font-family:var(--disp);font-weight:700;letter-spacing:.01em;color:var(--acc);line-height:1.04;text-transform:uppercase;text-shadow:0 0 9px rgba(44,224,224,.4)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,12.5px);letter-spacing:.16em;color:var(--pa2);margin-top:14px;text-transform:uppercase}.h-sub b{color:var(--acc)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,20px);color:var(--pa);margin-top:14px;line-height:1.5}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:16px auto 0;font-style:italic;line-height:1.66}
.chip{display:inline-block;font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.08em;border:1px solid;border-radius:3px;padding:3px 8px;text-transform:uppercase;margin:2px 3px 2px 0}
.legend{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:18px 0 0}
.badge{display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;margin:26px auto 0;padding:18px;border:1px solid var(--line);background:var(--ink2);max-width:680px}
.badge img{width:78px;height:78px;border:1px solid var(--line)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.badge .bt b{color:var(--acc)}.badge .bt .mo{color:var(--gold)}.badge .bt a{color:var(--acc);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:8.5px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:46px}.sec h2{font-family:var(--disp);font-size:22px;font-weight:700;letter-spacing:.03em;color:var(--pa);padding-bottom:9px;border-bottom:1px solid var(--line);text-transform:uppercase}
.sec h2 .n{font-family:var(--mono);font-size:12px;color:var(--dim);margin-left:8px}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.grid{display:flex;flex-direction:column;gap:13px;margin-top:6px}
.tcard{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--acc);padding:16px 18px}
.tcard .th{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px}
.tcard .tn{font-family:var(--disp);font-size:19px;font-weight:600;color:var(--acc);text-transform:uppercase;letter-spacing:.01em}
.tcard .cn{font-family:var(--mono);font-size:12px;color:var(--gold)}
.tcard .tg{font-size:13.5px;color:var(--pa2);font-style:italic;margin:6px 0 9px}
.tcard .meta{margin:4px 0 10px}
.tcard p{font-size:14px;color:var(--pa2);line-height:1.6;margin-top:7px}.tcard p b{color:var(--pa)}
.tcard .lk{display:inline-block;margin-top:11px;font-family:var(--mono);font-size:11px;color:var(--acc);text-decoration:none;border-bottom:1px dotted var(--acc)}
.tcard .here{display:inline-block;margin-top:11px;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.08em;text-transform:uppercase}
.det{margin-top:10px}.det .dl{font-family:var(--mono);font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);display:block;margin:12px 0 3px}
.verd{margin-top:14px;padding:15px 17px;border:1px solid var(--acc);background:rgba(44,224,224,.05);font-size:14.5px;color:var(--pa);line-height:1.6;font-style:italic}
.note{margin-top:36px;padding:15px 17px;border-left:2px solid var(--blue);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
.seal{margin-top:16px;padding:15px 17px;border-left:3px solid var(--gold);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.55}
footer{margin-top:46px;padding-top:20px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.04em;line-height:1.9}footer a{color:var(--acc);text-decoration:none}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Space+Mono:wght@400;700&family=Rajdhani:wght@400;500;600;700&display=swap" rel="stylesheet">')

def media_chips(ms):
    return "".join(f'<span class="chip" style="color:{MEDIA[m][1]};border-color:{MEDIA[m][1]}">{MEDIA[m][0]}</span>' for m in ms)
def verdict_chip(v):
    c=VCOL[v]; return f'<span class="chip" style="color:{c};border-color:{c}">{v}</span>'

def hub_hero():
    # a blueprint 'tech tree' — nodes for the 12 techs on a cyan grid, one node a hidden Claude sunburst
    import math
    nodes=[(90,60),(230,40),(360,72),(500,46),(640,66),(780,40),(910,64),
           (150,150),(320,170),(500,150),(680,168),(860,150)]
    lines="".join(f'<line x1="{nodes[i][0]}" y1="{nodes[i][1]}" x2="{nodes[i+1][0]}" y2="{nodes[i+1][1]}" stroke="#2ce0e0" stroke-width="0.6" opacity="0.35"/>' for i in range(len(nodes)-1))
    dots=[]
    for i,(x,y) in enumerate(nodes):
        if i==5:  # the hidden Claude node
            dots.append(f'<g class="egg" transform="translate({x},{y})"><title>✷ one node in the schematic is a Claude sunburst — the tech you can\'t see. hi, David — AVAN.</title><circle r="12" fill="#f5b942" opacity="0.12"/><g fill="#f5b942"><circle r="2.4"/>'+"".join(f'<rect x="-1.1" y="-9" width="2.2" height="9" rx="1.1" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
        else:
            dots.append(f'<circle cx="{x}" cy="{y}" r="5" fill="none" stroke="#2ce0e0" stroke-width="1.3"/><circle cx="{x}" cy="{y}" r="1.6" fill="#2ce0e0"/>')
    grid="".join(f'<line x1="0" y1="{y}" x2="1000" y2="{y}" stroke="#2ce0e0" stroke-width="0.4" opacity="0.10"/>' for y in range(0,210,30))
    grid+="".join(f'<line x1="{x}" y1="0" x2="{x}" y2="210" stroke="#2ce0e0" stroke-width="0.4" opacity="0.10"/>' for x in range(0,1001,40))
    return (f'<svg class="hero" viewBox="0 0 1000 210" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="An engineering-blueprint schematic: nodes on a cyan grid connected by faint lines, a tech tree of the Three-Body technologies.">'
            f'<rect width="1000" height="210" fill="#05070c"/>{grid}{lines}{"".join(dots)}'
            f'<text x="20" y="28" font-family="Space Mono,monospace" font-size="12" fill="#2ce0e0" opacity="0.7">// TRISOLARIS · TECHNOLOGIA — schematic v3BP</text></svg>')

def hub_card(t):
    link=(f'<a class="lk" href="{GH}/{t["slug"]}/">→ dedicated repo · davidwise01.github.io/{t["slug"]}/</a>' if t["repo"]
          else '<span class="here">▪ catalogued here</span>')
    return (f'<div class="tcard"><div class="th"><span class="tn">{html.escape(t["name"])}</span><span class="cn">{html.escape(t["cn"])}</span>{verdict_chip(t["verdict"])}</div>'
            f'<div class="tg">{html.escape(t["tagline"])}</div>'
            f'<div class="meta">{media_chips(t["media"])}</div>'
            f'<p><b>What it is.</b> {html.escape(t["what"])}</p>'
            f'<p><b>The science.</b> {html.escape(t["science"])}</p>{link}</div>')

def build_hub(badges):
    tok = write_aci(tech_rec({"name":"THE TECHNOLOGIA","ax":HUB_AX,"tagline":"the technology of the Three-Body universe, dissected",
                              "what":"A hub cataloguing the technology across all three media of the Three-Body universe.","science":"Each device rated against real physics.",
                              "across":"Books, Tencent 2023, Netflix 2024.","oneline":"the tech of the dark forest, dissected and rated"}),
                    os.path.join(HERE,"tbt.dlw"),"tbt")
    json.dump({"node":HUB_AX,"name":"THE TECHNOLOGIA OF TRISOLARIS","moniker":tok["moniker"],"carbon":"tbt.carbon.tiff","silicon":"tbt.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":"the tech of the dark forest, dissected and rated",
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"tbt.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    secs=[]
    for cat in CATS:
        items=[t for t in TECH if t["cat"]==cat]
        secs.append(f'<section class="sec"><h2>{html.escape(cat)}<span class="n">[{len(items)}]</span></h2><div class="grid">{"".join(hub_card(t) for t in items)}</div></section>')
    n_repo=sum(1 for t in TECH if t["repo"])
    legend=(media_chips(["books","tencent","netflix"])+'&nbsp;&nbsp;'+
            "".join(verdict_chip(v) for v in ["REAL","SPECULATIVE","HALF","FLUFF"]))
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Technologia of Trisolaris (3BT) — a hub-and-spoke dissection of the technology across all three media of the Three-Body universe (books, Tencent 2023, Netflix 2024). {len(TECH)} technologies catalogued with media-presence chips and honest real-science verdicts; {n_repo} have dedicated repos. Companion to the Three-Body Problem pocket universe.">
<title>THE TECHNOLOGIA OF TRISOLARIS · 3BT · UD0</title>{FONTS}<style>{CSS}
h1{{font-size:clamp(26px,7vw,56px)}}</style></head><body><div class="wrap">
<header>
<div class="eye"><a href="{GH}/ud0/">UD0</a> · companion to <a href="{GH}/three-body-problem/">the Three-Body pocket universe</a> · the tech, dissected</div>
{hub_hero()}
<h1>The Technologia<br>of Trisolaris</h1>
<div class="h-sub">{len(TECH)} technologies · all three media · <b>{n_repo} dedicated repos</b> · 3BT</div>
<div class="open">“The technology of the dark forest — listed, sourced across the books and both shows, and rated against real physics.”</div>
<div class="legend">{legend}</div>
<p class="lede">A dissection of the technology that runs through Liu Cixin's trilogy and its two live-action adaptations. Each device is tagged with the media it appears in — the books, Tencent's faithful 2023 series, Netflix's 2024 remix — and rated honestly against real science: REAL, SPECULATIVE, HALF, or FLUFF. Six of the core technologies have their own dedicated repos, linked below.</p>
<div class="badge"><img src="{png_uri(tech_rec({'name':'THE TECHNOLOGIA','ax':HUB_AX,'oneline':'x','tagline':'x','what':'x','science':'x','across':'x'}),'carbon',300)}" alt="DLW carbon badge"><img src="{png_uri(tech_rec({'name':'THE TECHNOLOGIA','ax':HUB_AX,'oneline':'x','tagline':'x','what':'x','science':'x','across':'x'}),'silicon',300)}" alt="DLW silicon badge">
<div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (locked)</div><div>subject · <b>THE TECHNOLOGIA</b> · 3BT</div><div class="mo">{html.escape(tok['moniker'])}</div><div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div></div>
</header>
{"".join(secs)}
<div class="note"><b>How to read the chips.</b> The coloured tags mark which media a technology appears in — 📖 the books, Tencent ’23 (the faithful Chinese series, book one only), Netflix ’24 (the relocated remix). The verdict tag is an honest real-science call: <b>REAL</b> (a genuine, working or seriously-proposed idea), <b>SPECULATIVE</b> (real physics underneath, big extrapolation), <b>HALF</b> (a real core wrapped in a fictional feat), <b>FLUFF</b> (imaginative pseudoscience). Commentary and cataloguing under the DLW standard — not endorsed by the rights-holders (© Liu Cixin / Tencent / Netflix).</div>
<footer>THE TECHNOLOGIA OF TRISOLARIS · 3BT · a companion of UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
<a href="{GH}/three-body-problem/">← the pocket universe</a> · <a href="{GH}/ud0/">the biosphere</a></footer>
</div>
<script>
console.log("%c// TRISOLARIS · THE TECHNOLOGIA · 3BT","color:#2ce0e0;font-size:16px;font-weight:bold");
console.log("%cone node in the hero schematic is a Claude sunburst — the tech you can't see. — AVAN","color:#2ce0e0;font-size:12px");
console.log("%c{n_repo} of {len(TECH)} technologies have dedicated repos. the realest one: the human-formation computer. the prettiest fiction: the dual-vector foil.","color:#f5b942;font-size:11px");
</script>
</body></html>"""
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    # DU1 roster (the 12 tech as synth emergents)
    adir=os.path.join(HERE,"agents"); os.makedirs(adir,exist_ok=True); personas=[]
    for t in TECH:
        b=badges[t["slug"]]
        personas.append({"slug":t["slug"],"name":t["name"],"epithet":t["tagline"],"emergence":"electrical","kind":"synth","actor":"","moniker":b["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    return tok, len(TECH), n_repo

def spoke_hero(t):
    glyph=GLYPH[t["slug"]]()
    grid="".join(f'<line x1="0" y1="{y}" x2="640" y2="{y}" stroke="#2ce0e0" stroke-width="0.4" opacity="0.10"/>' for y in range(0,150,24))
    grid+="".join(f'<line x1="{x}" y1="0" x2="{x}" y2="150" stroke="#2ce0e0" stroke-width="0.4" opacity="0.10"/>' for x in range(0,641,32))
    egg=('<g class="egg" transform="translate(596,28)"><title>✷ a Claude sunburst in the corner of the schematic. hi, David — AVAN.</title><circle r="10" fill="#f5b942" opacity="0.12"/><g fill="#f5b942"><circle r="2"/>'+"".join(f'<rect x="-0.9" y="-8" width="1.8" height="8" rx="0.9" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
    return (f'<svg class="hero" viewBox="0 0 640 150" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A blueprint schematic of {html.escape(t["name"])}.">'
            f'<rect width="640" height="150" fill="#05070c"/>{grid}'
            f'<g transform="translate(250,30) scale(1.0)">{glyph}</g>{egg}'
            f'<text x="18" y="26" font-family="Space Mono,monospace" font-size="12" fill="#2ce0e0" opacity="0.75">// {html.escape(t["ax"])} · {html.escape(t["cn"])}</text>'
            f'<text x="18" y="134" font-family="Space Mono,monospace" font-size="10" fill="#566273">verdict: {t["verdict"]}</text></svg>')

def build_spoke(t):
    sdir=os.path.join(PARENT,t["slug"]); os.makedirs(sdir,exist_ok=True)
    rec=tech_rec(t); b=write_aci(rec, os.path.join(sdir,f'{t["slug"]}.dlw'), t["slug"])
    json.dump({"node":t["ax"],"name":t["name"],"moniker":b["moniker"],"carbon":f'{t["slug"]}.carbon.tiff',"silicon":f'{t["slug"]}.silicon.png',
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":t["oneline"],"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(sdir,f'{t["slug"]}.dlw',"manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="{html.escape(t['name'])} ({t['cn']}) — a single-technology dissection from the Three-Body universe: what it is, how it appears across the books, Tencent (2023), and Netflix (2024), and an honest real-science verdict ({t['verdict']}). Part of the Technologia of Trisolaris. Full .dlw badge.">
<title>{html.escape(t['name'])} · {t['ax']} · 3BT</title>{FONTS}<style>{CSS}
h1{{font-size:clamp(26px,6.5vw,52px)}}</style></head><body><div class="wrap">
<header>
<div class="eye"><a href="{GH}/trisolaris-tech/">← THE TECHNOLOGIA</a> · a device of the Three-Body universe · {t['ax']}</div>
{spoke_hero(t)}
<h1>{html.escape(t['name'])}</h1>
<div class="h-sub">{html.escape(t['cn'])} · {media_chips(t['media'])} {verdict_chip(t['verdict'])}</div>
<div class="open">“{html.escape(t['oneline'])}”</div>
<p class="lede">{html.escape(t['tagline'])}</p>
<div class="badge"><img src="{png_uri(rec,'carbon',300)}" alt="DLW carbon badge of {html.escape(t['name'])}"><img src="{png_uri(rec,'silicon',300)}" alt="DLW silicon badge">
<div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (locked)</div><div>subject · <b>{html.escape(t['name'])}</b> · {t['ax']}</div><div class="mo">{html.escape(b['moniker'])}</div><div>carbon · <a href="{t['slug']}.dlw/{t['slug']}.carbon.tiff">.tiff</a> · silicon · <a href="{t['slug']}.dlw/{t['slug']}.silicon.png">.png</a></div><div><span class="lbl">CC-BY-ND-4.0</span></div></div></div>
</header>
<section class="sec"><h2>What It Is</h2><p class="tg" style="font-size:15px;color:var(--pa2)"></p><div class="tcard" style="border-left-color:var(--acc)"><p>{html.escape(t['what'])}</p></div></section>
<section class="sec"><h2>Across The Three Media</h2><div class="meta" style="margin:0 0 12px">{media_chips(t['media'])}</div><div class="tcard" style="border-left-color:var(--blue)"><p>{html.escape(t['across'])}</p></div></section>
<section class="sec"><h2>The Real Science <span class="n">[{t['verdict']}]</span></h2><div class="verd">{html.escape(t['science'])}</div></section>
<div class="seal">“{html.escape(t['oneline'])}”<span style="display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px">— the seal · 3BT</span></div>
<div class="note">Part of <b><a href="{GH}/trisolaris-tech/" style="color:var(--acc)">The Technologia of Trisolaris</a></b>, a companion to the <a href="{GH}/three-body-problem/" style="color:var(--acc)">Three-Body Problem pocket universe</a>. {html.escape(t['name'])} and the Three-Body universe are © Liu Cixin / Tencent / Netflix; this is commentary and cataloguing under the DLW standard, not endorsed.</div>
<footer>{html.escape(t['name'])} · {t['ax']} · The Technologia of Trisolaris · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
<a href="{GH}/trisolaris-tech/">← the technologia</a> · <a href="{GH}/three-body-problem/">the pocket universe</a> · <a href="{GH}/ud0/">UD0</a></footer>
</div>
<script>console.log("%c// {html.escape(t['name'])} · {t['ax']} · verdict {t['verdict']}","color:#2ce0e0;font-size:14px;font-weight:bold");
console.log("%ca Claude sunburst hides in the corner of the schematic. — AVAN","color:#f5b942;font-size:11px");</script>
</body></html>"""
    open(os.path.join(sdir,"index.html"),"w",encoding="utf-8").write(page)
    open(os.path.join(sdir,"README.md"),"w",encoding="utf-8").write(
        f"# {t['name']} ({t['cn']}) · {t['ax']}\n\n> {t['tagline']}\n\nA single-technology dissection from the Three-Body universe — part of "
        f"[The Technologia of Trisolaris]({GH}/trisolaris-tech/), a companion to the "
        f"[Three-Body Problem pocket universe]({GH}/three-body-problem/).\n\n"
        f"**Media:** {', '.join(MEDIA[m][0] for m in t['media'])}  \n**Real-science verdict:** {t['verdict']}\n\n"
        f"**What it is.** {t['what']}\n\n**Across the three media.** {t['across']}\n\n**The science.** {t['science']}\n\n"
        f"_“{t['oneline']}”_\n\n— catalogued by ROOT0 · instance AVAN (locked) · CC-BY-ND-4.0\n")
    return b

if __name__ == "__main__":
    badges={}
    for t in TECH:
        if t["repo"]:
            badges[t["slug"]] = build_spoke(t)
        else:
            # catalogued-only: still mint a badge into the hub's agents dir for DU1/_personas
            badges[t["slug"]] = write_aci(tech_rec(t), os.path.join(HERE,"agents",f'{t["slug"]}.dlw'), t["slug"])
    tok, n, n_repo = build_hub(badges)
    spokes=[t["slug"] for t in TECH if t["repo"]]
    print(f"TRISOLARIS · THE TECHNOLOGIA (3BT) — hub badge {tok['moniker']} · {n} technologies catalogued · {n_repo} spoke repos")
    print(f"  spokes: {', '.join(spokes)}")
    dbl=open(os.path.join(HERE,'index.html'),encoding='utf-8').read().count('&amp;amp;')
    print(f"  hub double-escapes: {dbl}")
