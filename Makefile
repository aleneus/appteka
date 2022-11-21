.PHONY: docs test

PACKAGE_FOLDER = appteka

all: help

help:
	@echo "check"
	@echo "cover"
	@echo "lint"
	@echo "ver"
	@echo "upload"
	@echo "uml"
	@echo "docs"

check: test fixme flake lint-e

test:
	@nose2 -vvv --with-coverage

fixme:
	@rgrep "TODO" -n \
		--include="*py" \
		--include="*rst" \
		--include="*md" \
		--exclude-dir=env \
		--exclude="release-checklist.md" \
		|| true

	@rgrep "# REF" -n \
		--include="*py" \
		--exclude-dir=env \
		|| true

flake:
	flake8 $(PACKAGE_FOLDER)

lint-e:
	pylint --disable=R,C,W $(PACKAGE_FOLDER) || true

cover:
	@nose2 --with-coverage --coverage-report=html

lint:
	pylint $(PACKAGE_FOLDER) || true

docs:
	sphinx-build docs/source/ docs/build/

ver:
	@cat $(PACKAGE_FOLDER)/__init__.py | grep __version__

upload:
	python3 setup.py sdist
	python3 -m twine upload --repository pypi dist/*

uml:
	pyreverse3 $(PACKAGE_FOLDER) -o png
