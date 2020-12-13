FROM python:3.6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

RUN pip install --no-cache-dir flask

COPY . /usr/src/app/

CMD ["python", "app.py"]
