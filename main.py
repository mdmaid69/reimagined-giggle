import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"