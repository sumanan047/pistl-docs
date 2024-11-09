# pistl-docs creation

---

### 1.0 Build the pistl-docs from package code (docstrings) using sphinx autodoc

Ensure you are at in the root of the pistl-docs repo.

Grab the necessary pistl version and dependencies defined in the poetry `pyproject.toml` file:
```commandline
poetry install
```
 
Build the docs with `sphinx-build` from scratch
```
sphinx-build -b html docs/source docs/build
```

