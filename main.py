import array
def get_array_length(array):
        return len(array)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"