from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)