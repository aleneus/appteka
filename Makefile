PACKAGE = appteka

.PHONY: flake uml release

all: help

help:
	@echo "make flake"
	@echo "make uml"
	@echo "make release ver=value"

flake:
	@flake8 $(PACKAGE)

uml:
	@pyreverse3 $(PACKAGE) -o png

release:
	@echo $(ver)
	hg up default
	hg merge develop
	hg ci -m 'merge from develop'
	hg tag $(ver)
	hg up develop
