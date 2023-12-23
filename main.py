def calculate_power(work, time):
        return work / time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"