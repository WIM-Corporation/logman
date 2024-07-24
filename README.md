# pylog

## Run Tests

### pytest

```bash
pip install pytest
python -m unittest discover -s tests -p 'test_*.py'
```

### tox

```bash
pip install tox pytest
tox
```

## Documentation

### Sphinx

```bash
pip install Sphinx sphinx-autobuild sphinx-rtd-theme
cd docs
make html
```
