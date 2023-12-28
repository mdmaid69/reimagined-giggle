  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"