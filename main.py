import array
def get_array_slice(array, i, j):
        return array[i:j]
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"