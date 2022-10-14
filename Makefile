install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

tests:
	poetry run pytest

coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

gendiff:
	poetry run gendiff