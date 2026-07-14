# Presentation Prompting, Styles, and QA

## Style presets

- **Editorial:** warm off-white, ink, restrained accents, generous whitespace.
- **Edu Warm:** ivory, clay orange, blue/green accents, example-first layouts.
- **Academic Clean:** graphite, calm blue, structured evidence and figure callouts.
- **Neon Circuit:** dark navy, cyan/violet, restrained system diagrams.
- **JDN Editorial:** editorial education storytelling with muted cyan, violet, and orange.
- **Hand-drawn Explainer:** paper background, clean ink, one or two marker accents.

## Production prompt

```text
Create ONE independent 16:9 presentation slide, slide NN of TT.
Purpose and audience: [locked context].
Visual style: [locked profile].
Slide role and claim: [role and one claim].
Render this Traditional Chinese text exactly: [exact title and short text].
Layout: [approved title position, text region, visual region, grid or columns, whitespace, page-number position, and density].
Style consistency: [approved palette, typography hierarchy, imagery or diagram language, chart treatment, logo treatment, and global avoid list].
Assets: [specific provided assets only].
Constraints: one slide only; readable text; no contact sheet, watermark, random text, extra slide number, unrelated logo, fake metrics, unsupported claim, or unapproved asset.
```

## QA

- Brief, outline, text, and sample are approved before generation.
- Outline count, manifest count, approved image count, and final PDF page count are identical.
- Exact 16:9 framing and one slide only.
- Text matches outline; no garbling, truncation, or tiny text.
- One main claim and the approved role-appropriate layout.
- Title placement, grid, text region, visual region, whitespace, page number, and density match the page layout description.
- Palette, typography mood, hierarchy, illustration or diagram language, chart treatment, logo treatment, and contrast match the approved profile without repeating identical composition.
- Required assets are present, undistorted, and rights-cleared.
- No overlap, watermark, unapproved logo, fake UI, or fabricated data.

Regenerate only the failing slide. If the global style changes, create a new profile version and approve a new sample first. Do not package a PDF while an outline field, source status, page layout, style rule, text freeze, or approval is incomplete.
