import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_datetime():
  return "%s" % datetime.datetime.now()

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)
