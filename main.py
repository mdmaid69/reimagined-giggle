import os
def list_files_in_directory(path):
        return os.listdir(path)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"