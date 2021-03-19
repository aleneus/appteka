# Release checklist

## Test

* All passed: `make check`
* Coverage >= 60%: `make check`

## Code

* No TODO notes: `make todo`
* No flakes: `make flake`
* No lint errors: `make lint-e`
* Lint result >= 9.55: `make lint`
* Old deprecated code is removed (todo list)

## Docs

* Successful build: `make docs`
* History is updated: `head -n 20 docs/source/history.rst`
* All necessary modules are included

## Distribution

* Actual version: `make ver`
* Dependencies are relevant: `setup.py`
* Installation successful: `python3 setup.py install --user`
