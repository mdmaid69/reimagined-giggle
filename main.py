import array
def reverse_array(array):
        array.reverse()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"