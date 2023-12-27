def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"