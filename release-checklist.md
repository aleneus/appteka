# Release checklist

## Code

* No `TODO` in the source code
* All unit tests passed (`make check`)
* The coverage by tests is not less than 40%
* No flakes (`make flake`)
  - Note: unused imports are allowed in deprecated modules
* The result of pylint is not less than 9.3 (`make lint`)
* No errors from pylint (`make lint-e`)
* Actual version in __init__.py
* All dependencies are relevant in setup.py

## Docs

* Docs is successfully built (`make docs`)
* All necessary modules are included to docs
* History is updated in docs

## Installation

* Installation successful (`python3 setup.py install --user`)
