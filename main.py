import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"