  import os
  def get_base_name(path):
        return os.path.basename(path)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"