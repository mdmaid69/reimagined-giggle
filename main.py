from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)