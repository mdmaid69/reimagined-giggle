def is_palindrome(s):
        return s == s[::-1]
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"