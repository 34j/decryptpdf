from pathlib import Path

import click
from tqdm import tqdm

from . import decrypt_pdf


@click.command()
@click.help_option("-h", "--help")
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "-p",
    "--password",
    type=str,
    prompt=True,
    hide_input=True,
    help="The password to decrypt the PDF file.",
)
def cli(path: str, password: str) -> None:
    """Decrypts a PDF file.
    If PATH is a directory, recursively searches for PDF files.
    If PATH is a file and does not exist, checks if PATH with ".pdf" extension exists.
    If the file is not encrypted, skips it.
    """
    path_ = Path(path)

    # If the path is a directory, recursively search for PDF files.
    # If not found, check if the path is a file and if it has a PDF extension.
    if path_.is_dir():
        input_paths = list(path_.rglob("*.pdf"))
        if len(input_paths) == 0:
            raise FileNotFoundError(f"No PDF files found in {path_}.")
    elif path_.exists():
        input_paths = [path_]
    elif path_.with_suffix(".pdf").exists():
        input_paths = [path_.with_suffix(".pdf")]
    else:
        raise FileNotFoundError(f"File {path_} does not exist.")

    pbar = tqdm(input_paths, desc="Decrypting PDF files", disable=len(input_paths) == 1)
    for input_path in pbar:
        output_path = input_path.with_suffix(".decrypted.pdf")
        try:
            decrypt_pdf(input_path, output_path, password)
        except Exception as e:
            pbar.write(f"Failed to decrypt {input_path}: {e}")
