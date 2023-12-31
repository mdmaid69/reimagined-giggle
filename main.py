from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)