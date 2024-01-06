import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"