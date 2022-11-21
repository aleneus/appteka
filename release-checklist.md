# Release checklist

## Auto check

* No errors: `make check`
* Coverage by tests >= 71%

## Code quality

* Lint result >= 9.9: `make lint`
* Old deprecated code is removed

## Docs

* Successful build: `make docs`
* History is updated: `head -n 20 docs/source/history.rst`

## Distribution

* Actual version: `make ver`
* Dependencies are relevant: `setup.py`
* Installation successful: `python3 setup.py install --user`
