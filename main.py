from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}