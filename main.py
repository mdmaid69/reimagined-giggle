  import os
  def delete_file(file_name):
        os.remove(file_name)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"