from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time