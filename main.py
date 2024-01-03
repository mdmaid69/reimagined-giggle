import array
def convert_array_to_bytes(array):
        return array.tobytes()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"