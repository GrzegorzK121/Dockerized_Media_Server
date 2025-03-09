FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install flask docker sqlite3 psutil

VOLUME [ "/files" ]

CMD ["python", "server.py"]
