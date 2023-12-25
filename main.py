from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)