import os
def remove_directory(path):
        os.rmdir(path)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"