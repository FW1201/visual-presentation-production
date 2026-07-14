---
name: visual-presentation-production
description: Create image-based 16:9 presentations through mandatory brief, exact page-count, outline-layout, style-lock, sample, per-slide generation, QA, and PDF-only delivery gates. Use for talks, workshops, lesson decks, reports, explainers, or branded presentations where each slide is a complete host-generated image.
---

# Visual Presentation Production

Create one complete 16:9 image per slide. Require an approved brief, a page-count-matched outline with layout descriptions, and a locked visual profile before generating any visual. Deliver one PDF only.

## Host Contract

Use only the host's native image-generation capability for slide visuals. Never use an image API, API key, external image CLI, HTML/CSS, SVG, or Python to draw slides. Bundled scripts may validate images and assemble approved full-slide images into one PDF.

In ChatGPT Work, request the host's available file-generation capability for one PDF only. Do not offer PPTX, Google Slides, speaker notes, or PNG bundles. If native image generation or PDF creation is unavailable, deliver the approved outline, manifest, and prompts, explain the capability gap, and stop.

Install this ZIP from the ChatGPT profile menu: **Skills → New skill → Upload from your computer**. A ZIP attached to a Work conversation is reference material, not an installer. Do not attempt to write to a personal skill directory, run bundled scripts, or install packages in ChatGPT Work.

## Start

Offer Quick, Guided (default), or Art director mode. Read `references/alignment-and-manifest.md` before asking for content or outlining and `references/prompting-styles-and-qa.md` before creating a style profile, prompt, or visual.

## Non-negotiable gates

Never infer a missing brief field, start an outline, create a manifest, write a production prompt, or generate a visual before the required gate is approved. Treat a user request such as “make a presentation about X” as an intake trigger, not authorization to begin production.

Ask one concise gate at a time in Guided mode. Quick mode may collect the same fields in one compact form, but still display the completed brief and require explicit approval. Art director mode adds per-page direction; it never bypasses a gate.

## Required brief gate

Collect and confirm all fields below. Show missing fields explicitly and ask only for those fields. If the user has no page-count preference, propose 6 pages and ask for confirmation.

1. Purpose, audience, setting, and duration.
2. Content source and organization: user outline, attached source material, or explicit permission for a proposed structure.
3. Exact `slide_count`, language, and 1920×1080 / 16:9 format.
4. Visual direction: uploaded logo, brand guide, existing deck, or reference image; otherwise ask the user to select a preset.
5. Rights and permitted use of all uploaded materials.

For source-free proposals, label every factual claim, number, case, or citation that lacks user material as `待確認`. Do not turn it into an asserted fact or generate it as final slide content until the user confirms it.

## Workflow

1. **Approve the brief.** Collect every required brief field. Summarize it, list the exact confirmed page count, and obtain approval. Do not continue when a required field is missing.
2. **Lock visual direction.** Ask for reference assets first. If none are supplied, offer 2–3 presets, including JDN Editorial as an optional preset. Record the chosen direction in a draft `visual-style-profile.md`.
3. **Propose the exact-count outline.** Create `outline.md` with exactly `slide_count` headings in the required format from `references/alignment-and-manifest.md`. Every page must state its role, one claim, exact visible text, source status, visual and assets, concrete layout description, and style rules.
4. **Approve the outline and text.** Present the complete page list and ask for approval. Do not create a manifest, sample, or prompt if the number of outline pages differs from `slide_count`, a layout description is missing, a source is `待確認`, or the user has not approved it. Freeze visible text only after approval.
5. **Lock the profile and manifest.** Complete `visual-style-profile.md` and create `deck-manifest.json` from the approved outline. The manifest must use the PDF-only delivery schema and repeat the exact page count.
6. **Approve one representative sample.** Generate one content slide with the locked profile. Inspect typography mood, grid, whitespace, contrast, imagery, page-number treatment, logo treatment, density, and readability. Update the profile only after approval.
7. **Generate one slide at a time.** Use one self-contained prompt per page. Apply the locked profile and the page's approved layout and style rules. Never create a multi-slide sheet.
8. **QA and targeted repair.** Check every page against its outline, layout, and the global profile. Regenerate only failed pages. A global style change requires a new profile version and a new approved sample.
9. **Produce the PDF.** In Codex or another local host, run `scripts/assemble_visual_deck.py` against the approved outline, manifest, and selected PNGs. In ChatGPT Work, use only the available native PDF path. Do not provide alternative deliverables.
10. **Deliver and continue.** Deliver `presentation.pdf` and `qa-report.json`. Ask whether to reuse the style profile for a new deck; reuse requires a new brief, exact page-count approval, and a new sample.

## Output Contract

Use 1920×1080 PNG only as internal approved-image inputs. Name them `slide_01.png`, `slide_02.png`, and so on. The only user-facing delivery is `presentation.pdf`.

```text
<project>/
├── selected/slide_01.png ...
├── prompts/
├── outline.md
├── deck-manifest.json
├── visual-style-profile.md
├── presentation.pdf
└── qa-report.json
```

## Codex-only technical packaging

Run this only in Codex or another local environment that supports Python and Pillow. Never run it in ChatGPT Work.

```bash
python3 scripts/assemble_visual_deck.py \
  --input-dir selected \
  --outline outline.md \
  --manifest deck-manifest.json \
  --pdf presentation.pdf \
  --report qa-report.json
```
