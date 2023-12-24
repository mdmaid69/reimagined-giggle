import re
def split_string(pattern, string):
        return re.split(pattern, string)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"