  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"