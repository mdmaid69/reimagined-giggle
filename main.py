  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"