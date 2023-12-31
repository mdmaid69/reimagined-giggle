import sys
def print_python_version():
        print(sys.version)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"