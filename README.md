# Introduction

This is an empty Python project example for github to serve as a boilerplate.
It aims to free users from repetitive engineering work and make users focus on features.

Following features are considered
- Python Package boilerplate.
- Github Actions CI
- pre-commit checking.
- Git Ignore



# Development Guidance

## pre-commit checking.
This example has integrated pre-commit, which will make it easier for developers to format and check their code.
Just run the following two commands, and the code will be automatically formatted using black and flake8 when the git commit command is executed.

```bash
pip install -e .[dev]
pre-commit install
```

## Installation

As a developer, you often want make changes to this package and hope it would reflect directly in your environment without reinstalling it. You can install it in editable mode with following command.
The `[dev]` option will help you to install some related packages when developing this package (e.g. flake8, black)

```bash
pip install -e .[dev]
```
