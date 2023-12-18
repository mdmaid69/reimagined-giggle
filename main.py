import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"