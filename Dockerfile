FROM python:3.12.2-bullseye as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --target=/install -r requirements.txt

COPY . .

FROM python:3.12.2-bullseye

COPY --from=builder /install /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app

ENV PYTHONPATH=/app

EXPOSE 8000
CMD ["python", "main.py"]
