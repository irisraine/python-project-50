# Gendiff

### Hexlet tests and linter status:
[![Actions Status](https://github.com/irisraine/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/irisraine/python-project-50/actions)
[![Actions Status](https://github.com/irisraine/python-project-50/workflows/pytest/badge.svg)](https://github.com/irisraine/python-project-50/actions/workflows/pytest.yml)
[![Actions Status](https://github.com/irisraine/python-project-50/workflows/flake8/badge.svg)](https://github.com/irisraine/python-project-50/actions/workflows/flake8.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/d0541db9f0767d6b5c43/maintainability)](https://codeclimate.com/github/irisraine/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d0541db9f0767d6b5c43/test_coverage)](https://codeclimate.com/github/irisraine/python-project-50/test_coverage)

### Description

Educational project. The command line utility compares two .json or .yaml files and gets a difference between them. Three types of difference format output are available.

### Installation

1. Clone git repository to your local machine: `git clone git@github.com:irisraine/python-project-50.git`
2. Go to the utility directory: `cd python-project-50`
3. You must have Poetry to build the project. Use `make build` command for creating the package.
4. For installation use `python3 -m pip install --user dist/*.whl` command, or `make package-install`

### Run

Use command `gendiff -f [format] file1 file2` to get a difference between `file1` and `file2`
Select one of specific formats (`stylish`, `plain`, `json`) to get a corresponding output type.
If you need a help, use command `gendiff -h`

### Demonstration

*Compare and get a difference between two flat .json files in stylish format:*
[![asciicast](https://asciinema.org/a/522467.svg)](https://asciinema.org/a/522467)

*Compare and get a difference between two flat .yaml files in stylish format:*
[![asciicast](https://asciinema.org/a/522469.svg)](https://asciinema.org/a/522469)

*Compare and get a difference between two flat .json files in plain format:*
[![asciicast](https://asciinema.org/a/522475.svg)](https://asciinema.org/a/522475)

*Compare and get a difference between two flat .yaml files in plain format:*
[![asciicast](https://asciinema.org/a/522476.svg)](https://asciinema.org/a/522476)

*Compare and get a difference between two flat .json files in json format:*
[![asciicast](https://asciinema.org/a/522477.svg)](https://asciinema.org/a/522477)

*Compare and get a difference between two flat .yaml files in json format:*
[![asciicast](https://asciinema.org/a/522478.svg)](https://asciinema.org/a/522478)

*Compare and get a difference between two nested .json files in stylish format:*
[![asciicast](https://asciinema.org/a/522480.svg)](https://asciinema.org/a/522480)

*Compare and get a difference between two nested .yaml files in stylish format:*
[![asciicast](https://asciinema.org/a/522481.svg)](https://asciinema.org/a/522481)

*Compare and get a difference between two nested .json files in plain format:*
[![asciicast](https://asciinema.org/a/522482.svg)](https://asciinema.org/a/522482)

*Compare and get a difference between two nested .yaml files in plain format:*
[![asciicast](https://asciinema.org/a/522483.svg)](https://asciinema.org/a/522483)

*Compare and get a difference between two nested .json files in json format:*
[![asciicast](https://asciinema.org/a/522486.svg)](https://asciinema.org/a/522486)

*Compare and get a difference between two nested .yaml files in json format:*
[![asciicast](https://asciinema.org/a/522490.svg)](https://asciinema.org/a/522490)