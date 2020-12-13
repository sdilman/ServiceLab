FROM python:3.6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

RUN pip install --no-cache-dir flask
RUN pip install --no-cache-dir requests

COPY . /usr/src/app/

CMD ["python", "app.py"]