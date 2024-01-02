  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"