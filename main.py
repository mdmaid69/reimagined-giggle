from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def calculate_circumference_circle(r):
        return 2 * 3.14 * r