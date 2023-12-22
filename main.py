def calculate_average(lst):
        return sum(lst) / len(lst)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"