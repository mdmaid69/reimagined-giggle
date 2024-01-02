from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)