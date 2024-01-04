import array
def check_if_array_contains_item(array, item):
        return item in array
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"