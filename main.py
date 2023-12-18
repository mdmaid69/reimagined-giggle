import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"