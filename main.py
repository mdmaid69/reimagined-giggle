import tensorflow as tf
print(tf.__version__)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"