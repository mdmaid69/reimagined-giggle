import array
def get_array_item_count(array, item):
        return array.count(item)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"