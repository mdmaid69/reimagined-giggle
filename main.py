import getpass
def get_username():
        return getpass.getuser()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"