from pathlib import Path

import pikepdf


def decrypt_pdf(input_path: Path, output_path: Path, password: str) -> None:
    """Decrypts a PDF file."""
    pdf = pikepdf.open(input_path, password=password, allow_overwriting_input=True)

    if not pdf.is_encrypted:
        raise ValueError(f"File {input_path} is not encrypted.")

    pdf.save(output_path)
    pdf.close()
