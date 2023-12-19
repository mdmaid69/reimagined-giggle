import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"