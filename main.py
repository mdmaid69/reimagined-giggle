import collections
def create_user_list():
        return collections.UserList()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"