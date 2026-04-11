# Batch all files in one call - each convert() spawns a JVM process, so repeated calls are slow.
from pathlib import Path

import opendataloader_pdf

ROOT_DIR = Path(__file__).parent
OUTPUT_DIR = ROOT_DIR / "markdown"

# Find all PDFs in the current folder and subfolders.
all_pdf_files = sorted(
    file
    for file in ROOT_DIR.rglob("*.pdf")
    if OUTPUT_DIR not in file.parents
)

# Avoid re-processing duplicate copies with the same file name.
unique_by_name: dict[str, Path] = {}
for pdf_file in all_pdf_files:
    unique_by_name.setdefault(pdf_file.name, pdf_file)

pdf_files = list(unique_by_name.values())

if not pdf_files:
    print("No PDF files found to convert.")
else:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    opendataloader_pdf.convert(
        input_path=pdf_files,
        output_dir=str(OUTPUT_DIR),
        # image_output="embedded",
        format="markdown",
    )
    print(f"Converted {len(pdf_files)} PDF file(s) into: {OUTPUT_DIR}")