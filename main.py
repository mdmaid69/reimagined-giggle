import array
def set_array_item(array, i, item):
        array[i] = item
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"