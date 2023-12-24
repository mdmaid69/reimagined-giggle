from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps