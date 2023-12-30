def find_min(lst):
        return min(lst)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"