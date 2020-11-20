# Release checklist

## Tests

* All passed (`make check`)
* Coverage >= 51% (`htmlcov`)

## Code

* No `TODO`
* No flakes (`make flake`)
  - Note: unused imports are allowed in deprecated modules
* No lint errors (`make lint-e`)
* Lint result >= 9.35 (`make lint`)

## Docs

* Docs is successfully built (`make docs`)
* All necessary modules are included to docs
* History is updated in docs

## Distr

* Actual version  (`__init__.py`)
* Dependencies are relevant (`setup.py`)
* Installation successful (`python3 setup.py install --user`)
