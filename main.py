import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"