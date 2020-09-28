PACKAGE = appteka

.PHONY: docs

all: help

help:
	@echo "check"
	@echo "flake"
	@echo "lint"
	@echo "lint-e"
	@echo "upload"
	@echo "uml"
	@echo "docs"

check:
	python3 test/test_waveform.py
	python3 test/test_multiwaveform.py
	python3 test/test_phasor.py
	python3 test/test_editor.py

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
