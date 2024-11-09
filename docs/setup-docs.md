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

### 2.0 Build the docs in a Docker environment

```commandline
docker build -t pistl-docs:latest .
```

Test the docs build by running the container in detached mode and using the current directory as source.
```commandline
docker run --rm -p 8000 -d pistl-docs:latest
```

<blockquote>
Debug the container by running bash inside of it and mounting the current directory to the container to run commands

```commandline
docker run --rm -v .:/pistl-docs -p 8000 -it pistl-docs:latest bash
```
</blockquote>