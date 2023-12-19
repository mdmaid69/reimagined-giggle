from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity