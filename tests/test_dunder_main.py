import subprocess  # noqa: S404
import sys


def test_can_run_as_python_module():
    """Run the CLI as a Python module."""
    result = subprocess.run(
        [sys.executable, "-m", "decryptpdf", "--help"],
        check=True,
        capture_output=True,
        shell=False,
    )
    assert result.returncode == 0
    assert b"decryptpdf [OPTIONS]" in result.stdout
