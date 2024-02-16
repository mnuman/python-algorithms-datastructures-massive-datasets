install:
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	python -m black .

lint:
	python -m flake8 .

test:
	python -m pytest -vv .

run:
	python random_bloom.py

all:	install format lint test run
	


