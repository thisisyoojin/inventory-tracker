FROM python:3.12.7-slim-bullseye

RUN pip install poetry==1.8.2

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install

EXPOSE 8000

COPY tracker ./tracker

ENTRYPOINT [ "poetry", "run", "python", "./tracker/manage.py", "runserver", "0.0.0.0:8000" ]