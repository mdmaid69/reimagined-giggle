import array
def get_array_typecode(array):
        return array.typecode
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"