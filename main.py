from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)