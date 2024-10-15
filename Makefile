install:
	pip install --upgrade pip
	pip install -U pytest

test:
	pytest -q test_helper_functions.py