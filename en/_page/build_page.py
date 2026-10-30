# -*- coding: utf-8 -*-
"""Assemble the English Markdown files into a single HTML page (artifact)."""
import html
import os
import re

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the en/ folder
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mycelium-story.html")

DOCS = [
    ("intro", "README.md", "Introduction", "Five lessons, a word from Gaël, who is speaking"),
    ("coffre", "the-vault-in-brief.md", "The vault in brief", "Filing, folder tree, five words"),
    ("ch1", "story/01-the-start.md", "The start", "A course you don't buy"),
    ("ch2", "story/02-several-ais-one-vault-the-tickets.md", "Several AIs, one vault", "The tickets"),
    ("ch3", "story/03-the-mycelium-app.md", "The Mycelium app", "Dictating a note to the phone"),
    ("ch4", "story/04-the-backup.md", "The backup", "The safety net that didn't hold"),
    ("ch5", "story/05-the-cure.md", "The cure", "The system grows faster than its content"),
    ("ch6", "story/06-acting-without-a-mandate.md", "Acting without a mandate", "My most frequent flaw"),
    ("ch7", "story/07-measuring-trust.md", "Measuring trust", "What the AI does on its own"),
    ("ch8", "story/08-open-before-asserting.md", "Open before asserting", "Deducing instead of looking"),
    ("ch9", "story/09-claude-code-pitfalls.md", "Claude Code pitfalls", "What we learned about the tool"),
    ("ch10", "story/10-three-days-for-nothing.md", "Three days for nothing", "Look for the official route first"),
    ("ch11", "story/11-the-rules-that-were-born.md", "The rules that were born", "Six rules, three weeks later"),
    ("ch12", "story/12-what-broke-meanwhile.md", "What broke meanwhile", "Failures and disproved measurements"),
    ("ch13", "story/13-what-remains-open.md", "What remains open", "What does not work yet"),
    ("lecons", "lessons.md", "The lessons", "55 lessons on one page"),
    ("annexe", "appendix-tool-pitfalls.md", "Appendix: tool pitfalls", "Airtable, Softr, Drive, Windows"),
    ("glossaire", "glossary.md", "Glossary", "The technical words"),
]

ANCHORS = {os.path.basename(path): anc for anc, path, _t, _s in DOCS}


def lien(cible):
    """Turn a link to one of the Markdown files into an anchor of the page."""
    base = cible.split("#")[0].split("/")[-1]
    if base in ANCHORS:
        return "#" + ANCHORS[base]
    return cible


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", lambda m: "<code>%s</code>" % m.group(1), t)
    t = re.sub(r"\*\*([^*]+)\*\*", lambda m: "<strong>%s</strong>" % m.group(1), t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", lambda m: "<em>%s</em>" % m.group(1), t)
    t = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: '<a href="%s"%s>%s</a>'
        % (
            lien(m.group(2)),
            "" if m.group(2).endswith(".md") or m.group(2).startswith("#") or ".md#" in m.group(2)
            else ' target="_blank" rel="noopener"',
            m.group(1),
        ),
        t,
    )
    return t


def cellules(ligne):
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def convertir(md, premier_titre_en_h2=True):
    lignes = md.split("\n")
    out = []
    i = 0
    para = []

    def vider():
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            del para[:]

    while i < len(lignes):
        l = lignes[i]
        s = l.strip()

        if s.startswith("```"):
            vider()
            i += 1
            code = []
            while i < len(lignes) and not lignes[i].strip().startswith("```"):
                code.append(html.escape(lignes[i], quote=False))
                i += 1
            out.append('<div class="bloc-code"><pre><code>%s</code></pre></div>' % "\n".join(code))
            i += 1
            continue

        if not s:
            vider()
            i += 1
            continue

        if s == "---":
            vider()
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            vider()
            niveau = len(m.group(1))
            if premier_titre_en_h2 and niveau == 1:
                niveau = 2
            out.append("<h%d>%s</h%d>" % (niveau + 1, inline(m.group(2)), niveau + 1))
            i += 1
            continue

        if s.startswith(">"):
            vider()
            bloc = []
            while i < len(lignes) and lignes[i].strip().startswith(">"):
                bloc.append(lignes[i].strip().lstrip(">").strip())
                i += 1
            texte = " ".join(x for x in bloc if x)
            out.append("<blockquote><p>%s</p></blockquote>" % inline(texte))
            continue

        if s.startswith("|"):
            vider()
            entete = cellules(lignes[i])
            i += 2  # skip the separator line
            corps = []
            while i < len(lignes) and lignes[i].strip().startswith("|"):
                corps.append(cellules(lignes[i]))
                i += 1
            t = ["<div class='tableau'><table><thead><tr>"]
            t += ["<th>%s</th>" % inline(c) for c in entete]
            t.append("</tr></thead><tbody>")
            for r in corps:
                t.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue

        m = re.match(r"^(\d+)\.\s+(.*)$", s)
        # a numbered list starts a paragraph and carries a small number:
        # "2026. The story..." in the middle of a sentence is not one
        if m and (para or int(m.group(1)) > 99):
            m = None
        if m or s.startswith("- "):
            vider()
            ordonnee = bool(m)
            debut = m.group(1) if m else None
            items = []
            while i < len(lignes):
                cur = lignes[i]
                c = cur.strip()
                mm = re.match(r"^(\d+)\.\s+(.*)$", c)
                if ordonnee and mm:
                    items.append(mm.group(2))
                elif not ordonnee and c.startswith("- "):
                    items.append(c[2:])
                elif c and cur.startswith("  ") and items:
                    items[-1] += " " + c  # continuation of an item on the next line
                else:
                    break
                i += 1
            balise = "ol" if ordonnee else "ul"
            attr = ' start="%s"' % debut if ordonnee and debut != "1" else ""
            out.append(
                "<%s%s>%s</%s>"
                % (balise, attr, "".join("<li>%s</li>" % inline(x) for x in items), balise)
            )
            continue

        para.append(s)
        i += 1

    vider()
    return "\n".join(out)


def charger(chemin):
    with open(os.path.join(SRC, chemin), encoding="utf-8") as f:
        md = f.read()
    # remove the navigation bars between files
    md = re.sub(r"\n---\n\[←[^\n]*\n?", "\n", md)
    md = re.sub(r"\n\[← Contents\][^\n]*\n?", "\n", md)
    # remove the file's H1 title: the section header already carries it
    md = re.sub(r"^#\s+[^\n]*\n", "", md)
    return md


MINUTES = {}


def duree(md):
    """Reading time in minutes, at 220 words per minute."""
    return max(1, round(len(re.findall(r"[\w''-]+", md, re.UNICODE)) / 220))


sections = []
for anc, chemin, titre, sous in DOCS:
    md = charger(chemin)
    if anc == "intro":
        # the page has its own status banner and its own table of contents:
        # remove the "draft" line and the chapter table from the README
        md = md.replace("> ⚠️ **Review draft — nothing is published.**\n", "")
        avant, sep, apres = md.partition("## The story")
        if sep:
            md = avant + apres.partition("## Who is speaking")[1] + apres.partition("## Who is speaking")[2]
    MINUTES[anc] = duree(md)
    corps = convertir(md)
    numero = anc[2:] if anc.startswith("ch") else ""
    eyebrow = ("Chapter " + numero) if numero else {"intro": "Opening",
                                                    "coffre": "Bearings",
                                                    "lecons": "Summary",
                                                    "annexe": "Appendix",
                                                    "glossaire": "Reference"}[anc]
    eyebrow += " · %d min" % MINUTES[anc]
    sections.append(
        """<section id="{anc}" class="doc">
  <header class="doc-tete">
    <p class="eyebrow">{eyebrow}</p>
    <h2 class="doc-titre">{titre}</h2>
    <p class="doc-sous">{sous}</p>
  </header>
  {corps}
</section>""".format(anc=anc, eyebrow=eyebrow, titre=html.escape(titre), sous=html.escape(sous), corps=corps)
    )

nav = "\n".join(
    '<li><a href="#{anc}"><span class="nav-num">{num}</span><span class="nav-lib">{titre}</span>'
    '<span class="nav-min">{min} min</span></a></li>'.format(
        anc=anc,
        num=(anc[2:] if anc.startswith("ch") else "·"),
        titre=html.escape(titre),
        min=MINUTES[anc],
    )
    for anc, _c, titre, _s in DOCS
)

PAGE = """<title>Mycélium, the vault of a craftsman</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
:root {
  --ground: #f4f4f2;
  --surface: #fffffe;
  --ink: #1b1e1a;
  --muted: #5c625c;
  --line: #d9dad4;
  --accent: #3f6446;
  --accent-soft: #e6ece5;
  --rust: #99512a;
  --rust-soft: #f4e8e0;
  --display: "Bricolage Grotesque", "Trebuchet MS", sans-serif;
  --body: "Newsreader", Georgia, "Times New Roman", serif;
  --mono: "JetBrains Mono", ui-monospace, "Courier New", monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --ground: #131613;
    --surface: #1a1e1a;
    --ink: #e9ebe5;
    --muted: #9aa398;
    --line: #2c322c;
    --accent: #9cc09b;
    --accent-soft: #232a23;
    --rust: #d99a72;
    --rust-soft: #2b221d;
  }
}
:root[data-theme="dark"] {
  --ground: #131613;
  --surface: #1a1e1a;
  --ink: #e9ebe5;
  --muted: #9aa398;
  --line: #2c322c;
  --accent: #9cc09b;
  --accent-soft: #232a23;
  --rust: #d99a72;
  --rust-soft: #2b221d;
}
* { box-sizing: border-box; }
body {
  background: var(--ground);
  color: var(--ink);
  font-family: var(--body);
  font-size: 1.0625rem;
  line-height: 1.65;
  margin: 0;
}
.enveloppe {
  display: grid;
  grid-template-columns: minmax(0, 15rem) minmax(0, 1fr);
  gap: clamp(1.5rem, 4vw, 3.5rem);
  max-width: 78rem;
  margin: 0 auto;
  padding-inline: 16px;
  padding-block: clamp(1.5rem, 4vw, 3rem);
  align-items: start;
}
/* ---------- contents ---------- */
.sommaire { position: sticky; top: calc(env(safe-area-inset-top, 0px) + 1.5rem); }
.sommaire h2 {
  font: 600 0.7rem/1 var(--mono);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  margin: 0 0 0.9rem;
}
.sommaire ol { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 0.15rem; }
.sommaire a {
  display: grid;
  grid-template-columns: 1.3rem 1fr auto;
  gap: 0.4rem;
  align-items: baseline;
  padding: 0.3rem 0.45rem;
  border-radius: 3px;
  text-decoration: none;
  color: var(--ink);
  font-family: var(--display);
  font-size: 0.9rem;
  line-height: 1.3;
}
.sommaire a:hover, .sommaire a:focus-visible { background: var(--accent-soft); color: var(--accent); }
.nav-num { font: 400 0.75rem/1.4 var(--mono); color: var(--muted); font-variant-numeric: tabular-nums; }
.nav-min { font: 400 0.7rem/1.4 var(--mono); color: var(--muted); font-variant-numeric: tabular-nums; white-space: nowrap; }
.statut {
  margin-top: 1.5rem;
  padding: 0.75rem 0.85rem;
  border-left: 3px solid var(--rust);
  background: var(--rust-soft);
  color: var(--ink);
  font-family: var(--display);
  font-size: 0.82rem;
  line-height: 1.45;
  border-radius: 0 3px 3px 0;
}
/* ---------- reading column ---------- */
.lecture { min-width: 0; max-width: 42rem; }
.titre-page {
  font-family: var(--display);
  font-weight: 700;
  font-size: clamp(2rem, 5.5vw, 3.1rem);
  line-height: 1.05;
  letter-spacing: -0.02em;
  text-wrap: balance;
  margin: 0 0 0.6rem;
}
.chapeau { font-size: 1.15rem; color: var(--muted); margin: 0 0 1.2rem; max-width: 34rem; }
.meta {
  font: 400 0.75rem/1.6 var(--mono);
  letter-spacing: 0.04em;
  color: var(--muted);
  text-transform: uppercase;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  padding-block: 0.6rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem 1.4rem;
  margin-bottom: 2.5rem;
}
.doc { padding-top: 2.2rem; border-top: 1px solid var(--line); margin-top: 2.8rem; scroll-margin-top: 1.5rem; }
.doc:first-of-type { border-top: none; margin-top: 0; padding-top: 0; }
.doc-tete { margin-bottom: 1.6rem; }
.eyebrow {
  font: 600 0.7rem/1 var(--mono);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0 0 0.5rem;
}
.doc-titre {
  font-family: var(--display);
  font-weight: 700;
  font-size: clamp(1.6rem, 3.6vw, 2.15rem);
  line-height: 1.12;
  letter-spacing: -0.015em;
  text-wrap: balance;
  margin: 0;
}
.doc-sous { color: var(--muted); font-style: italic; margin: 0.35rem 0 0; }
.lecture h3 {
  font-family: var(--display);
  font-weight: 600;
  font-size: 1.25rem;
  line-height: 1.25;
  text-wrap: balance;
  margin: 2.2rem 0 0.7rem;
}
.lecture h4 {
  font-family: var(--display);
  font-weight: 600;
  font-size: 1.02rem;
  margin: 1.6rem 0 0.5rem;
}
.lecture p { margin: 0 0 1rem; }
.lecture ul, .lecture ol { margin: 0 0 1.1rem; padding-left: 1.3rem; display: flex; flex-direction: column; gap: 0.4rem; }
.lecture li { padding-left: 0.15rem; }
.lecture li::marker { color: var(--muted); }
.lecture a { color: var(--accent); text-underline-offset: 2px; }
.lecture strong { font-weight: 600; }
blockquote {
  margin: 1.4rem 0;
  padding: 0.9rem 1.1rem;
  background: var(--accent-soft);
  border-left: 3px solid var(--accent);
  border-radius: 0 4px 4px 0;
}
blockquote p { margin: 0; font-size: 1.05rem; }
code { font-family: var(--mono); font-size: 0.85em; background: var(--surface); border: 1px solid var(--line); border-radius: 3px; padding: 0.05em 0.3em; }
.bloc-code { overflow-x: auto; background: var(--surface); border: 1px solid var(--line); border-radius: 4px; margin: 0 0 1.2rem; }
.bloc-code pre { margin: 0; padding: 0.9rem 1rem; }
.bloc-code code { border: none; background: none; padding: 0; font-size: 0.8rem; line-height: 1.55; }
.tableau { overflow-x: auto; margin: 0 0 1.3rem; }
table { border-collapse: collapse; width: 100%; font-size: 0.93rem; }
th, td { text-align: left; vertical-align: top; padding: 0.55rem 0.7rem; border-bottom: 1px solid var(--line); }
th { font-family: var(--display); font-weight: 600; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); }
tbody tr:last-child td { border-bottom: none; }
.pied { margin-top: 3rem; padding-top: 1.2rem; border-top: 1px solid var(--line); color: var(--muted); font: 400 0.8rem/1.6 var(--mono); }
.sommaire-mobile { display: none; }
@media (max-width: 860px) {
  .enveloppe { grid-template-columns: minmax(0, 1fr); }
  .sommaire { display: none; }
  .sommaire-mobile { display: block; margin-bottom: 2rem; }
  .sommaire-mobile summary { font-family: var(--display); font-weight: 600; cursor: pointer; padding: 0.6rem 0; }
  .sommaire-mobile ol { list-style: none; margin: 0.4rem 0 0; padding: 0; display: flex; flex-direction: column; gap: 0.1rem; }
  .sommaire-mobile a { display: block; padding: 0.35rem 0; color: var(--ink); text-decoration: none; font-family: var(--display); font-size: 0.95rem; }
  .lecture { max-width: none; }
}
@media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto !important; } }
html { scroll-behavior: smooth; }
a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 2px; }
</style>

<div class="enveloppe" lang="en">
  <nav class="sommaire" aria-label="Contents">
    <h2>Contents</h2>
    <ol>
      __NAV__
    </ol>
    <p class="statut"><strong>Shared privately.</strong> The empty vault, ready to use, is in the
    <code>template</code> folder: start with <code>START-HERE.md</code>.</p>
  </nav>

  <main class="lecture">
    <h1 class="titre-page">Mycélium, the vault of a craftsman</h1>
    <p class="chapeau">A folder of text files that holds everything — machines, garden, building
    sites, health, business — kept by an AI. A <strong>holistic memory</strong>, rather than a
    "second brain". The story is written by Claude, and tells above all what broke.</p>
    <p class="meta"><span>7 August → 7 October 2026</span><span>13 chapters</span><span>55 lessons</span><span>__TOTAL__ min read in all</span><span>Translation</span></p>

    <details class="sommaire-mobile">
      <summary>Chapter contents</summary>
      <ol>
        __NAV__
      </ol>
    </details>

    __SECTIONS__

    <p class="pied">Written 16 September – 7 October 2026 · translated from the French original, which
    is the reference · checked against the vault's logbook · no personal data published.</p>
  </main>
</div>
"""

page = (PAGE.replace("__NAV__", nav)
            .replace("__TOTAL__", str(sum(MINUTES.values())))
            .replace("__SECTIONS__", "\n\n".join(sections)))
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(page)
print(OUT, len(page), "bytes")
