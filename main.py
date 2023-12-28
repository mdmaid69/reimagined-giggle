from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)