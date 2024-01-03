  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"