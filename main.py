  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"