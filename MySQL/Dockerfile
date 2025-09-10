FROM python:3.12-slim

# install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app/

# Copy uv.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./uv.lock* /app/

# TODO: don't install dev dependencies
RUN uv sync --frozen --no-cache

ENV PYTHONPATH=/app

COPY ./my_app /app/my_app

EXPOSE 8080

CMD ["/app/.venv/bin/fastapi", "run", "my_app/main.py", "--host", "0.0.0.0", "--port", "8080"]
# CMD ["uvicorn", "my_app.main:app", "--host", "0.0.0.0", "--port", "8080"]

