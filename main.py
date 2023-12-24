def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"