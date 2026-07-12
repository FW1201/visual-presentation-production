---
name: visual-presentation-production
description: Create image-based 16:9 presentations through outline, format, visual-style, sample, per-slide generation, QA, speaker-note, and assembly gates. Use for talks, workshops, lesson decks, reports, explainers, or branded presentations where each slide is a complete host-generated image and the final delivery may include PNG, PDF, PPTX, or Google Slides.
---

# Visual Presentation Production

Create one complete 16:9 image per slide. Prefer visual coherence over object-level editability.

## Host Contract

Use only the host's native image-generation capability for slide visuals. Never use an image API, API key, external image CLI, HTML/CSS, SVG, or Python to draw slides. Bundled scripts may validate images and place approved full-slide images into PDF/PPTX containers.

In ChatGPT Work, create Google Slides only when the relevant app and action are available. Otherwise deliver PNG and PDF. Do not promise native PowerPoint creation in Work. If native image generation is unavailable, deliver the outline, manifest, and prompts, then stop.

Install this ZIP from the ChatGPT profile menu: **Skills → New skill → Upload from your computer**. A ZIP attached to a Work conversation is reference material, not an installer. Do not attempt to write to a personal skill directory, run bundled scripts, or install packages in ChatGPT Work.

## Start

Offer Quick, Guided (default), or Art director mode. Read `references/alignment-and-manifest.md` before outlining and `references/prompting-styles-and-qa.md` before generating.

## Workflow

1. Align purpose, audience, source material, slide count, language, 16:9 pixel size, outputs, speaker notes, brand assets, and reuse intent.
2. Create `outline.md` with one key claim, exact text, visual role, layout intent, and required assets per slide. Freeze visible text before batch generation.
3. Create `visual-style-profile.md`; offer 2–3 directions if none is given. Include JDN Editorial as an optional preset, never a forced default.
4. Create `deck-manifest.json` using the reference schema.
5. Generate one representative content slide as the sample. Obtain explicit approval before generating other slides.
6. Create one self-contained prompt per slide and generate one 16:9 image at a time. Never create a multi-slide sheet.
7. Inspect and repair only failing slides for text, truncation, source alignment, style drift, asset misuse, or unwanted marks.
8. Optionally write `speech.md` with one section per slide.
9. In Codex or another host with local code execution, optionally run `scripts/assemble_visual_deck.py` to validate and produce PPTX/PDF. The script places images full-bleed and does not draw slide content. In ChatGPT Work, do not run this script; deliver PNG/PDF or use the available Google Slides action instead.
10. Deliver all artifacts and ask whether to reuse the same style profile for a new deck. Reuse requires a new sample slide.

## Output Contract

Default to 1920×1080 PNG. Name images `slide_01.png`, `slide_02.png`, and so on.

```text
<project>/
├── selected/slide_01.png ...
├── final/slide_01.png ...
├── prompts/
├── outline.md
├── deck-manifest.json
├── visual-style-profile.md
├── speech.md             # optional
├── presentation.pptx     # optional
└── presentation.pdf      # optional
```

## Codex-only technical packaging

Run this only in Codex or another local environment that supports Python and the bundled dependencies. Never run it in ChatGPT Work.

```bash
python3 scripts/assemble_visual_deck.py \
  --input-dir selected \
  --manifest deck-manifest.json \
  --out-dir final \
  --pptx presentation.pptx \
  --pdf presentation.pdf
```
