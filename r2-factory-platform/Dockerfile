FROM python:3-slim

WORKDIR /app

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock ./

COPY ../r2-factory-platform ./r2-factory-platform/

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

RUN pip uninstall -y poetry

COPY ../r2-factory-platform .

EXPOSE 8000

CMD gunicorn main:app -b 0.0.0.0:8080 --workers=2 --threads=2 --worker-class=gthread

