from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import array
def get_array_as_list(array):
        return list(array)