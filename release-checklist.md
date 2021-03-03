# Release checklist


## Test

* All passed: `make check`
* Coverage >= 58%: `make check`

## Code

* No TODO notes: `make todo`
* No flakes: `make flake`
* No lint errors: `make lint-e`
* Lint result >= 9.40: `make lint`
* Old deprecated code is removed (todo list)

## Docs

* Docs is successfully built (`make docs`)
* All necessary modules are included to docs
* History is updated in docs

## Distr

* Actual version  (`__init__.py`)
* Dependencies are relevant (`setup.py`)
* Installation successful (`python3 setup.py install --user`)
