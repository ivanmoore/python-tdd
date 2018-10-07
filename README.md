# TDD in python

Having cloned this repo, open a terminal and `cd` into this repo.

## Installation and examples

```bash
pip install virtualenv # use "sudo" if you have to
virtualenv -p python3 venv
source venv/bin/activate
```

### "nosetests" test runner

```bash
pip install nose
nosetests test/sample_test.py
nosetests test # i.e. all tests in the "test" folder
```

### (optional) "py.test" test runner

With better output when running single test
```bash
pip install pytest
py.test test/sample_test.py
py.test test # i.e. all tests in the "test" folder
```

## When you've finished

When you don't want to use the virtual environment any more - i.e. the end of this lab:
```bash
deactivate
```
