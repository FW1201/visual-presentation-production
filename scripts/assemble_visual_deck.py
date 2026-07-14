#!/usr/bin/env python3
"""Validate an approved 16:9 deck and assemble its single PDF delivery."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError as error:
    raise SystemExit("Pillow is required: python3 -m pip install pillow") from error


OUTLINE_HEADING = re.compile(r"^## Slide (\d+) of (\d+)\s*$", re.MULTILINE)
LAYOUT_FIELDS = (
    "structure",
    "title_position",
    "text_region",
    "visual_region",
    "whitespace",
    "page_number_position",
    "density",
)
SOURCE_STATUSES = {"provided", "user-confirmed"}


def load_manifest(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read manifest: {error}") from error


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def expected_ids(count: int) -> list[str]:
    return [str(index).zfill(2) for index in range(1, count + 1)]


def validate_outline(path: Path, count: int) -> list[str]:
    errors: list[str] = []
    try:
        outline = path.read_text(encoding="utf-8")
    except OSError as error:
        return [f"Cannot read outline: {error}"]
    headings = OUTLINE_HEADING.findall(outline)
    ids = [item[0].zfill(2) for item in headings]
    totals = [int(item[1]) for item in headings]
    if len(headings) != count:
        errors.append("outline must contain exactly slide_count headings in '## Slide NN of TT' format")
    if ids != expected_ids(count):
        errors.append("outline slide ids must be sequential from 01 through slide_count")
    if any(total != count for total in totals):
        errors.append("every outline heading total must equal slide_count")
    return errors


def validate_slide(slide: object, expected_id: str) -> list[str]:
    if not isinstance(slide, dict):
        return [f"slide_{expected_id} must be an object"]
    errors: list[str] = []
    if str(slide.get("id", "")).zfill(2) != expected_id:
        errors.append(f"slide ids must be sequential; expected {expected_id}")
    for field in ("role", "claim", "title", "visual"):
        if not nonempty(slide.get(field)):
            errors.append(f"slide_{expected_id}.{field} must be a non-empty string")
    text = slide.get("text")
    if not isinstance(text, list) or any(not nonempty(item) for item in text):
        errors.append(f"slide_{expected_id}.text must be a list of non-empty strings")
    if slide.get("source_status") not in SOURCE_STATUSES:
        errors.append(f"slide_{expected_id}.source_status must be provided or user-confirmed")
    layout = slide.get("layout")
    if not isinstance(layout, dict):
        errors.append(f"slide_{expected_id}.layout must be an object")
    else:
        for field in LAYOUT_FIELDS:
            if not nonempty(layout.get(field)):
                errors.append(f"slide_{expected_id}.layout.{field} must be a non-empty string")
    style_rules = slide.get("style_rules")
    if not isinstance(style_rules, list) or not style_rules or any(not nonempty(item) for item in style_rules):
        errors.append(f"slide_{expected_id}.style_rules must be a non-empty list of strings")
    if slide.get("approved") is not True:
        errors.append(f"slide_{expected_id}.approved must be true")
    return errors


def validate_manifest(data: dict) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    count = data.get("slide_count")
    if not isinstance(count, int) or count < 1:
        errors.append("slide_count must be an integer of at least 1")
        return errors
    if data.get("width_px") != 1920 or data.get("height_px") != 1080:
        errors.append("this version requires 1920x1080 output")
    for field in ("brief_approved", "source_review_complete", "outline_approved", "sample_approved", "all_text_frozen"):
        if data.get(field) is not True:
            errors.append(f"{field} must be true")
    if not nonempty(data.get("style_profile_version")):
        errors.append("style_profile_version must be a non-empty string")
    delivery = data.get("delivery")
    if delivery != {"format": "PDF", "filename": "presentation.pdf"}:
        errors.append("delivery must be exactly {'format': 'PDF', 'filename': 'presentation.pdf'}")
    sample_slide = str(data.get("sample_slide", "")).zfill(2)
    if sample_slide not in expected_ids(count):
        errors.append("sample_slide must identify one slide in the approved range")
    slides = data.get("slides")
    if not isinstance(slides, list) or len(slides) != count:
        errors.append("slides must contain exactly slide_count rows")
        return errors
    for slide, identifier in zip(slides, expected_ids(count)):
        errors.extend(validate_slide(slide, identifier))
    return errors


def normalize(source: Path) -> Image.Image:
    with Image.open(source) as raw:
        raw.load()
        if abs(raw.width / raw.height - 16 / 9) > 0.02:
            raise ValueError(f"{source.name} is not 16:9")
        image = raw.convert("RGB")
    image = ImageOps.contain(image, (1920, 1080), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (1920, 1080), "white")
    canvas.paste(image, ((1920 - image.width) // 2, (1080 - image.height) // 2))
    return canvas


def write_pdf(images: list[Image.Image], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    images[0].save(destination, "PDF", save_all=True, append_images=images[1:], resolution=150)


def write_report(path: Path, valid: bool, count: int | None, errors: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "valid": valid,
        "delivery": "presentation.pdf",
        "expected_slide_count": count,
        "outline_page_count": count if valid else None,
        "pdf_page_count": count if valid else None,
        "errors": errors,
    }
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--outline", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    data = load_manifest(args.manifest)
    count = data.get("slide_count") if isinstance(data.get("slide_count"), int) else None
    errors = validate_manifest(data)
    if count is not None and count >= 1:
        errors.extend(validate_outline(args.outline, count))

    images: list[Image.Image] = []
    if not errors and count is not None:
        for identifier in expected_ids(count):
            source = args.input_dir / f"slide_{identifier}.png"
            if not source.exists():
                errors.append(f"missing slide_{identifier}.png")
                continue
            try:
                images.append(normalize(source))
            except (OSError, ValueError) as error:
                errors.append(str(error))

    try:
        if not errors:
            write_pdf(images, args.pdf)
        write_report(args.report, not errors, count, errors)
    finally:
        for image in images:
            image.close()

    if errors:
        print("Validation failed:\n" + "\n".join(f"- {item}" for item in errors))
        return 1
    print(f"Created {count}-page PDF at {args.pdf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
