  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"