def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"