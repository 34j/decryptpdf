from pathlib import Path
from typing import Annotated

import pikepdf
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
    *,
    overwrite: Annotated[
        bool,
        typer.Option(
            "-o/-n",
            "--overwrite/--no-overwrite",
            help="Overwrite the original file, or save decrypted file as .decrypted.pdf",
        ),
    ] = True,
) -> None:
    """
    Decrypts a PDF file.

    If PATH is a directory, recursively searches for PDF files.
    If PATH is a file and does not exist, checks if PATH with ".pdf" extension exists.
    If the file is not encrypted, skips it.

    Raises:
        FileNotFoundError: If PATH does not identify any PDF files.

    """
    path_ = Path(path)

    # If the path is a directory, recursively search for PDF files.
    # If not found, check if the path is a file and if it has a PDF extension.
    if path_.is_dir():
        input_paths = [p for p in path_.rglob("*") if p.suffix.lower() == ".pdf"]
        if len(input_paths) == 0:
            raise FileNotFoundError(f"No PDF files found in {path_}.")
    elif path_.exists():
        input_paths = [path_]
    elif path_.with_suffix(".pdf").exists():
        input_paths = [path_.with_suffix(".pdf")]
    elif path_.with_suffix(".PDF").exists():
        input_paths = [path_.with_suffix(".PDF")]
    else:
        raise FileNotFoundError(f"File {path_} does not exist.")

    pbar = tqdm(input_paths, desc="Decrypting PDF files", disable=len(input_paths) == 1)
    failed = 0
    for input_path in pbar:
        output_path = input_path if overwrite else input_path.with_suffix(".decrypted.pdf")
        try:
            decrypt_pdf(input_path, output_path, password)
        except (OSError, ValueError, pikepdf.PikepdfError) as error:
            failed += 1
            pbar.write(f"Failed to decrypt {input_path}: {error}")
    if failed:
        raise typer.Exit(code=1)
