def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"