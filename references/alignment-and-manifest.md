# Presentation Alignment and Manifest

## Brief gate

Before outlining, collect and explicitly approve purpose, audience, setting, duration, content source mode, exact page count, language, visual references or preset, and material rights. Report missing fields rather than assuming them. A source-free proposal may contain `待確認` items, but they must be confirmed before outline approval.

## Outline contract

Use exactly one heading per page in this format: `## Slide 01 of 06`. The declared total and number of headings must exactly equal the approved `slide_count`.

Each page must include:

```text
- Role: [cover / context / evidence / process / example / close]
- Claim: [one claim]
- Visible text: [exact title and short body, or none]
- Source status: [provided / user-confirmed]
- Visual and assets: [what must appear]
- Layout: [title position; text region; visual region; grid or columns; whitespace; page-number position; density]
- Style rules: [how this page follows the global profile]
```

Do not approve an outline with a missing page, non-sequential page identifier, missing layout, empty style rules, unresolved source status, or page count mismatch.

## `deck-manifest.json`

```json
{
  "schema_version": 2,
  "project_id": "example-deck",
  "brief_approved": false,
  "source_review_complete": false,
  "outline_approved": false,
  "slide_count": 6,
  "width_px": 1920,
  "height_px": 1080,
  "style_profile_version": "1.0",
  "sample_slide": "03",
  "sample_approved": false,
  "all_text_frozen": false,
  "delivery": {
    "format": "PDF",
    "filename": "presentation.pdf"
  },
  "slides": [
    {
      "id": "01",
      "role": "cover",
      "claim": "",
      "title": "",
      "text": [],
      "source_status": "provided",
      "visual": "",
      "layout": {
        "structure": "",
        "title_position": "",
        "text_region": "",
        "visual_region": "",
        "whitespace": "",
        "page_number_position": "",
        "density": ""
      },
      "assets": [],
      "style_rules": [],
      "approved": false
    }
  ]
}
```

Require exactly `slide_count` sequential rows (`01` through the approved total). Preserve user-approved exact text. Record attachments by portable file name or role, never by machine-specific absolute path.

## Style profile

`visual-style-profile.md` is the single source of truth for style. Record id/version, palette, typography mood and hierarchy, grid, layout rhythm, whitespace, illustration and diagram language, chart form, page-number rule, brand and source assets, density, prohibited elements, approved sample, and prompt scaffold. Each page's `style_rules` may vary composition for its role but must preserve those global rules.
