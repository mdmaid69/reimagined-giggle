import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"