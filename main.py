from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)