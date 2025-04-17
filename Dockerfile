FROM python:3.12-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3","main.py"]
EXPOSE 9667

