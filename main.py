import array
def get_array_as_int(array):
        return int(array[0])
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"