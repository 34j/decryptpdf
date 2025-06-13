from pathlib import Path
from typing import Annotated

import typer
from tqdm import tqdm

from . import decrypt_pdf

app = typer.Typer(
    name="decryptpdf",
    help="Decrypt PDF files using a password.",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command()
def cli(
    path: Annotated[Path, typer.Argument()],
    password: Annotated[
        str,
        typer.Option(
            "-p",
            "--password",
            prompt=True,
            hide_input=True,
            help="The password to decrypt the PDF file.",
        ),
    ],
    overwrite: Annotated[
        bool,
        typer.Option(
            "-o/-n",
            "--overwrite/--no-overwrite",
            help="Overwrite the original file, "
            "or save decrypted file as .decrypted.pdf",
        ),
    ] = True,
) -> None:
    """
    Decrypts a PDF file.

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
        if overwrite:
            output_path = input_path
        else:
            output_path = input_path.with_suffix(".decrypted.pdf")
        try:
            decrypt_pdf(input_path, output_path, password)
        except Exception as e:
            pbar.write(f"Failed to decrypt {input_path}: {e}")
