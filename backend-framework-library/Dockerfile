FROM python:3-slim

WORKDIR /app

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock ./

COPY ../backend-framework-library ./backend-framework-library/

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

RUN pip uninstall -y poetry

COPY . .

EXPOSE 8000

CMD gunicorn main:app -b 0.0.0.0:8080 --workers=2 --threads=2 --worker-class=gthread

