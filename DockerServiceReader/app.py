import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def call_service():
  contents = requests.get("http://web_service:8080").content.decode("utf-8")
  with open('test_output.txt', 'w') as f:
    f.write(contents)
  return contents

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8090, debug=True)