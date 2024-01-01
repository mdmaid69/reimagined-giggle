import collections
def create_user_dict():
        return collections.UserDict()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"