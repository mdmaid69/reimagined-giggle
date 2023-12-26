import collections
def create_user_string():
        return collections.UserString()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"