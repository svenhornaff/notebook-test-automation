# Jupyter Notebook - CI/CD, test automation (regression) using testbook

automated Jupyter Notebook testing (regression) using mypy, flake8, tox, git action and testbook

[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
[![CI Automated Testing](https://github.com/svenhornaff/python-test-automation/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/svenhornaff/python-test-automation/actions/workflows/python-app.yml)

### step 1: get the repo

```zsh
git clone https://github.com/svenhornaff/notebook-test-automation.git
```

### step 2: create a venv in the repo directory

```
python -m venv venv
```

### step 3: activate yor venv

```zsh
ource venv/bin/activate
```

### step 4: install requirements

```zsh
pip install requirements.txt
```

### step 4: run your tests

```zsh
pytest -v
```
