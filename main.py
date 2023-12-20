from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)