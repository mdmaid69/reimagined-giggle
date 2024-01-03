from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time