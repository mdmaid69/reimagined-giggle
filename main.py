import array
def insert_into_array(array, i, item):
        array.insert(i, item)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"