PACKAGE = appteka

.PHONY: check style flakes lint upload uml

all: help

help:
	@echo "make check"
	@echo "make style"
	@echo "make flakes"
	@echo "make lint"
	@echo "make upload"

	@echo "make uml"

check:
	python3 test/test_waveform.py
	python3 test/test_multiwaveform.py
	python3 test/test_phasor.py
	python3 test/test_editor.py

style:
	pycodestyle $(PACKAGE)

flakes:
	pyflakes $(PACKAGE)

lint:
	pylint $(PACKAGE)

upload:
	python3 setup.py sdist upload

uml:
	pyreverse3 $(PACKAGE) -o png
