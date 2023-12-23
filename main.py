  import os
  def split_path(path):
        return os.path.split(path)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"