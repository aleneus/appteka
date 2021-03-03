PACKAGE = appteka

.PHONY: docs

all: help

help:
	@echo "check"
	@echo "cover"
	@echo "todo"
	@echo "flake"
	@echo "lint"
	@echo "lint-e"
	@echo "upload"
	@echo "uml"
	@echo "docs"

check:
	@nose2 -vvv --with-coverage

cover:
	@nose2 --with-coverage --coverage-report=html

todo:
	@rgrep "TODO" --include="*py" --include="*md" --include="*rst" --exclude="release-checklist.md" || true

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
