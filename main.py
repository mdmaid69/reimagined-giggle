import os
def get_file_size(filename):
        return os.path.getsize(filename)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"