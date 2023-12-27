def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"