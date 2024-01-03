from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal