import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"