import sys
def add_to_python_path(path):
        sys.path.append(path)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"