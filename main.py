import array
def get_array_as_tuple(array):
        return tuple(array)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"