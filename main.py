from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import os
  def get_current_working_directory():
        return os.getcwd()