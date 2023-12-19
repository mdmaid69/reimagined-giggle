import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"