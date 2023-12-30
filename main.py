from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)