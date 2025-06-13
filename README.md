# decryptpdf

<p align="center">
  <a href="https://github.com/34j/decryptpdf/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/34j/decryptpdf/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://decryptpdf.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/decryptpdf.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/34j/decryptpdf">
    <img src="https://img.shields.io/codecov/c/github/34j/decryptpdf.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
</p>
<p align="center">
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/decryptpdf/">
    <img src="https://img.shields.io/pypi/v/decryptpdf.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/decryptpdf.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/decryptpdf.svg?style=flat-square" alt="License">
</p>

---

**Documentation**: <a href="https://decryptpdf.readthedocs.io" target="_blank">https://decryptpdf.readthedocs.io </a>

**Source Code**: <a href="https://github.com/34j/decryptpdf" target="_blank">https://github.com/34j/decryptpdf </a>

---

Simple CLI tool for decrypting PDF files.

## Installation

Install this via pip (or your favourite package manager):

```shell
pipx install decryptpdf
```

## Usage

```shell
> decryptpdf -h

 Usage: decryptpdf [OPTIONS] PATH

 Decrypts a PDF file.

 If PATH is a directory, recursively searches for PDF files. If PATH is a file and
 does not exist, checks if PATH with ".pdf" extension exists. If the file is not
 encrypted, skips it.

╭─ Arguments ──────────────────────────────────────────────────────────────────────╮
│ *    path      PATH  [default: None] [required]                                  │
╰──────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────╮
│ *  --password            -p                      TEXT  The password to decrypt   │
│                                                        the PDF file.             │
│                                                        [default: None]           │
│                                                        [required]                │
│    --overwrite           -o  --no-overwrite  -n        Overwrite the original    │
│                                                        file, or save decrypted   │
│                                                        file as .decrypted.pdf    │
│                                                        [default: o]              │
│    --install-completion                                Install completion for    │
│                                                        the current shell.        │
│    --show-completion                                   Show completion for the   │
│                                                        current shell, to copy it │
│                                                        or customize the          │
│                                                        installation.             │
│    --help                -h                            Show this message and     │
│                                                        exit.                     │
╰──────────────────────────────────────────────────────────────────────────────────╯
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- prettier-ignore-start -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-end -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)

This package was created with
[Copier](https://copier.readthedocs.io/) and the
[browniebroke/pypackage-template](https://github.com/browniebroke/pypackage-template)
project template.
