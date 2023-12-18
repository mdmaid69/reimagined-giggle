from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)