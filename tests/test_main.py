from pathlib import Path
from tempfile import TemporaryDirectory

import pikepdf
import pytest
from typer.testing import CliRunner

from decryptpdf import decrypt_pdf
from decryptpdf.cli import app


@pytest.mark.parametrize("overwrite", [True, False])
def test_command(overwrite: bool) -> None:
    with TemporaryDirectory() as dirname:
        filename = Path(dirname, "test.pdf")
        filename_out = Path(dirname, "test.pdf" if overwrite else "test.decrypted.pdf")
        pikepdf.new().save(
            filename,
            encryption=pikepdf.Encryption(owner="owner_password", user="user_password"),
        )
        runner = CliRunner()
        result = runner.invoke(
            app,
            [filename.as_posix(), "-p", "user_password", "-o" if overwrite else "-n"],
        )
        assert result.exit_code == 0
        pdf = pikepdf.open(filename_out)
        assert not pdf.is_encrypted
        pdf.close()


def test_decrypt() -> None:
    with TemporaryDirectory() as dirname:
        filename = Path(dirname, "test.pdf")
        filename_out = Path(dirname, "test.pdf")
        pikepdf.new().save(
            filename,
            encryption=pikepdf.Encryption(owner="owner_password", user="user_password"),
        )
        decrypt_pdf(filename, filename_out, "user_password")
        pdf = pikepdf.open(filename_out)
        assert not pdf.is_encrypted
        pdf.close()


def test_not_encrypted() -> None:
    with TemporaryDirectory() as dirname:
        filename = Path(dirname, "test.pdf")
        pikepdf.new().save(filename)
        with pytest.raises(ValueError):
            decrypt_pdf(filename, filename, "user_password")
