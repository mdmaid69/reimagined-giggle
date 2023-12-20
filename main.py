from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)