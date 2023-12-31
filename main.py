from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)