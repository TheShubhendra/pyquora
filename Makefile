.DEFAULT_GOAL := help
.PHONY: clean black lint test install

PIP             := pip

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf */__pycache__/
	rm -rf .pytest_cache
	rm -f .coverage
lint:
	flake8

black:
	black .

test:
	pytest --cov -v

install:
	$(PIP)  install -r requirements.txt -r requirements-dev.txt

help:
	@echo "Available targets:"
	@echo "- clean       Clean up the build and egg directories"
	@echo "- lint        Check style with flake8"
	@echo "- black       Check style with black"
	@echo "- test        Run tests using pytest"
	@echo
	@echo "Available variables:"
	@echo "- PIP         default: $(PIP)"
