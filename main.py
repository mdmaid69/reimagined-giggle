from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)