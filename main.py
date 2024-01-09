def reverse_list(lst):
        return lst[::-1]
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"