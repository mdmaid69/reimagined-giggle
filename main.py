import glob
def find_files(pattern):
        return glob.glob(pattern)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"