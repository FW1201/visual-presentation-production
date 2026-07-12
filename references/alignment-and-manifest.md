# Presentation Alignment and Manifest

## Alignment gates

1. Purpose, audience, setting, duration, and source hierarchy.
2. Slide count, language, 16:9 size, PNG/PDF/PPTX/Google Slides, notes, and output location.
3. Outline and exact visible text.
4. Visual style, brand assets, density, diagram treatment, and avoid list.
5. One approved representative sample slide.

## `deck-manifest.json`

```json
{
  "schema_version": 1,
  "project_id": "example-deck",
  "slide_count": 6,
  "width_px": 1920,
  "height_px": 1080,
  "sample_slide": "03",
  "sample_approved": false,
  "all_text_frozen": false,
  "outputs": ["PNG", "PPTX", "PDF"],
  "speaker_notes": true,
  "slides": [
    {
      "id": "01",
      "role": "cover",
      "title": "",
      "text": [],
      "visual": "",
      "layout": "",
      "assets": [],
      "approved": false
    }
  ]
}
```

Require exactly `slide_count` unique slide rows. Preserve user-approved exact text. Record attachments by portable file name or role, not machine-specific absolute path.

## Style profile

Record style id/version, palette, typography mood, layout rhythm, illustration/diagram language, brand and source assets, density, whitespace, prohibited elements, approved sample, and prompt scaffold.
