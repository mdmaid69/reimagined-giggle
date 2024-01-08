from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev