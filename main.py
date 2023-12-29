import array
def convert_array_to_string(array):
        return array.tostring()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"