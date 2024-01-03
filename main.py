def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"