FROM python:3.12-slim

RUN pip install \
    ruff \
    mypy \
    pytest \
    pytest-cov \
    bandit \
    pip-audit \
    radon \
    xenon \
    pylint

WORKDIR /app