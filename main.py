from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)