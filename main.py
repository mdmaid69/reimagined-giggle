from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def sort_numbers(numbers):
        return sorted(numbers)