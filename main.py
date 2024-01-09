def is_even(n):
        return n % 2 == 0
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"