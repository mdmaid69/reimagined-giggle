from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)