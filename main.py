from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets