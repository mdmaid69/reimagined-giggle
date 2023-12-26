import array
def get_array_as_set(array):
        return set(array)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"