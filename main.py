  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"