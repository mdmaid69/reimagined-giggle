import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"