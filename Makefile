PACKAGE = appteka

.PHONY: style flakes lint uml release upload diff

all: help

help:
	@echo "make diff"
	@echo "make style"
	@echo "make flakes"
	@echo "make lint"
	@echo "make uml"
	@echo "make upload"

diff:
	hg diff > diff.diff

style:
	pycodestyle $(PACKAGE)

flakes:
	pyflakes $(PACKAGE)

lint:
	pylint $(PACKAGE)

uml:
	pyreverse3 $(PACKAGE) -o png

upload:
	python3 setup.py sdist upload

check:
	python3 test/test_phasor.py
