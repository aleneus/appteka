PACKAGE = appteka

.PHONY: style flakes lint uml release upload

all: help

help:
	@echo "make style"
	@echo "make flakes"
	@echo "make lint"
	@echo "make uml"
	@echo "make upload"

style:
	pycodestyle $(PACKAGE)

flakes:
	pyflakes $(PACKAGE)

lint:
	pylint $(PACKAGE)

uml:
	pyreverse3 $(PACKAGE) -o png

check:
	python3 test/test_waveform.py
	python3 test/test_phasor.py
	python3 test/test_editor.py

upload:
	python3 setup.py sdist upload
