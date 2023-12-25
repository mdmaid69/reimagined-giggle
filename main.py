from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities