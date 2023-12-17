  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"