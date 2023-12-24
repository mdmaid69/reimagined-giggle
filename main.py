from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets