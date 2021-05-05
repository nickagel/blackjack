SHELL:=/usr/bin/env bash -O extglob -O globstar -o pipefail

.PHONY: default help
default help:
	@echo 'This Makefile has the following targets:'
	@grep -o  -E '^[a-zA-Z0-9\-]+( [a-zA-Z0-9\-]+)?:( |$$)' Makefile | sed -E 's/: ?//g' | tr ' ' '\n'

.PHONY: init
init:
	rm -rf venv
	python -m venv venv
	. venv/bin/activate
	pip install --upgrade pip wheel
	pip install -r requirements.txt

.PHONY: run
run:
	python src/api.py

.PHONY: format
format:
	black src/ test/

.PHONY: test
test:
	python -m pytest . -vvv