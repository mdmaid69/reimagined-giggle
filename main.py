def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"