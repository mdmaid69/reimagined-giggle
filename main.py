  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"