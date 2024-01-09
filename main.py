from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import array
def pop_from_array(array, i=-1):
        return array.pop(i)