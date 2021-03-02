PACKAGE = appteka

.PHONY: docs

all: help

help:
	@echo "todo"
	@echo "check"
	@echo "flake"
	@echo "lint"
	@echo "lint-e"
	@echo "upload"
	@echo "uml"
	@echo "docs"

todo:
	@rgrep "TODO" --include="*py" --include="*md" --exclude="release-checklist.md"

check:
	@nose2 -vvv --with-coverage --coverage-report=html

flake:
	flake8 $(PACKAGE)

lint:
	pylint $(PACKAGE)

lint-e:
	pylint --disable=R,C,W $(PACKAGE)

docs:
	sphinx-build docs/source/ docs/build/

upload:
	python3 setup.py sdist
	python3 -m twine upload --repository pypi dist/*

uml:
	pyreverse3 $(PACKAGE) -o png
