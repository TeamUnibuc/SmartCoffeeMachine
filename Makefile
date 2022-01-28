.PHONY: help test unit-test integration-test

.DEFAULT: help
help:
	@echo "make test"
	@echo "     run all the tests"
	@echo "make unit-test"
	@echo "     run unit tests"
	@echo "make integration-test"
	@echo "     run integration tests"

test:
	cd source; coverage run -m unittest; coverage xml

unit-test:
	cd source/tests/unit; python -m unittest

integration-test:
	cd source/tests/integration; python -m unittest
