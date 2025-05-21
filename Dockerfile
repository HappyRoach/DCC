FROM python:3.12-slim-bullseye AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim-bullseye

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY . .

RUN useradd -m appuser && chown -R appuser:appuser /app
RUN chmod +x start.sh
USER appuser

EXPOSE 9667
CMD ["./start.sh"]
