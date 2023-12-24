import array
def get_array_itemsize(array):
        return array.itemsize
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"