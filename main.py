import array
def extend_array(array, iterable):
        array.extend(iterable)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"