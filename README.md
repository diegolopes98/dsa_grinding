# DSA Grinding

Project to study data structures, algorithms and the most used language for it (python)

using [uv](https://github.com/astral-sh/uv) for dependency management

## Running Tests

### Problem Tests

Run tests with coverage for coding problems using the following command:

```sh
uv run python -m pytest problems/ --cov=problems --cov-report=html --cov-config=.coveragerc
```

### Data Structure Tests

Run tests with coverage for data structures using the following command:

```sh
uv run python -m pytest data_structures/ --cov=data_structures --cov-report=html --cov-config=.coveragerc
```

### All Tests

Run all tests with coverage using the following command:

```sh
uv run python -m pytest --cov=problems --cov=data_structures --cov-report=html --cov-config=.coveragerc
```
