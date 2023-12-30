from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)