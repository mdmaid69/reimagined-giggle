from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_roi(gain, cost):
        return (gain - cost) / cost