from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import array
def iterate_over_array(array):
        for item in array:
        print(item)