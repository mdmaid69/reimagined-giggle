from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)