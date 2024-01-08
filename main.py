  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"