FROM python:3.10

COPY . /pistl-docs

WORKDIR /pistl-docs

COPY . .

RUN pip install poetry; \
    poetry config virtualenvs.create false; \
    poetry install --with dev
RUN sphinx-build -b html docs/source docs/build

EXPOSE 8000

CMD ["python", "-m", "http.server", "8000", "--directory", "docs/build"]