# Contributing

## Installation

Setup for contributing to this project is as follows:

### 1. Clone the repository locally

```bash
git clone https://github.com/torchbox-forks/wagtailguide
```

### 2. Create a virtual environment and install the requirements

```bash
cd wagtailguide
python -m venv venv
source venv/bin/activate
pip install -e ".[testing,lint]"
```

### 3. Install the pre-commit hooks

```bash
pre-commit install
```

### 4. Do some work

Update the code, write some tests, etc.

You can run the tests and linting with `make test` and `make lint` respectively:

### 5. Coverage

To run the tests with coverage, run:

```bash
coverage run runtests.py
coverage html # to generate a coverage report you can view in your browser
```

## Submitting a pull request

Please ensure that your pull request includes the following:

- A description of the changes
- Tests for the changes
- Documentation for the changes (if applicable)

Make your pull request at <https://github.com/torchbox-forks/wagtailguide/pulls>
