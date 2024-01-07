from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import array
def get_array_index(array, item):
        return array.index(item)