from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)