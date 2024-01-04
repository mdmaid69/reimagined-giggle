import array
def get_bytes_from_array(array):
        return array.tobytes()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"