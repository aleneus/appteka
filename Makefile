PACKAGE = appteka

.PHONY: style flakes uml release

all: help

help:
	@echo "make style"
	@echo "make flakes"
	@echo "make uml"
	@echo "make release ver=value"

style:
	pycodestyle $(PACKAGE)

flakes:
	pyflakes $(PACKAGE)

uml:
	pyreverse3 $(PACKAGE) -o png

release:
	@echo $(ver)
	hg up default
	hg merge develop
	hg ci -m 'merge from develop'
	hg tag $(ver)
	hg up develop
