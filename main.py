def calculate_perpetuity(payment, rate):
        return payment / rate
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"