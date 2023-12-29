import array
def convert_array_to_unicode(array):
        return array.tounicode()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"