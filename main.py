def find_max(lst):
        return max(lst)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"