from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable