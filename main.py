import array
def clear_array(array):
        array *= 0
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"