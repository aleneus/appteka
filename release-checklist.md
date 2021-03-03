# Release checklist


## Test

* All passed: `make check`
* Coverage >= 59%: `make check`

## Code

* No TODO notes: `make todo`
* No flakes: `make flake`
* No lint errors: `make lint-e`
* Lint result >= 9.45: `make lint`
* Old deprecated code is removed (todo list)

## Docs

* Successful build: `make docs`
* History is updated: `head -n 20 docs/source/history.rst`
* All necessary modules are included

## Distr

* Actual version  (`__init__.py`)
* Dependencies are relevant (`setup.py`)
* Installation successful (`python3 setup.py install --user`)
