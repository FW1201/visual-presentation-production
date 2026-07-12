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
Layout and assets: [specific composition and provided assets].
Constraints: one slide only; readable text; no contact sheet, watermark, random text, extra slide number, unrelated logo, fake metrics, or unapproved asset.
```

## QA

- Exact 16:9 framing and one slide only.
- Text matches outline; no garbling, truncation, or tiny text.
- One main claim and role-appropriate layout.
- Style matches approved sample without repeating identical composition.
- Required assets are present, undistorted, and rights-cleared.
- No overlap, watermark, unapproved logo, fake UI, or fabricated data.

Regenerate only the failing slide. If the style changes, approve a new sample first.
