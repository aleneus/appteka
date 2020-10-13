PACKAGE = appteka

.PHONY: docs

all: help

help:
	@echo "check"
	@echo "cover"
	@echo "flake"
	@echo "lint"
	@echo "lint-e"
	@echo "upload"
	@echo "uml"
	@echo "docs"

check:
	@nose2 -vvv

cover:
	@nose2 --with-coverage --coverage-report=html

flake:
	flake8 $(PACKAGE)

lint:
	pylint $(PACKAGE)

lint-e:
	pylint --disable=R,C,W $(PACKAGE)

docs:
	sphinx-build docs/source/ docs/build/

upload:
	python3 setup.py sdist upload

uml:
	pyreverse3 $(PACKAGE) -o png
