import array
def convert_array_to_list(array):
        return array.tolist()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"