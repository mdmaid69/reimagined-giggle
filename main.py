def square_number(x):
        return x**2
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"