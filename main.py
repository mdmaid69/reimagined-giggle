import sys
def exit_program():
        sys.exit()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"