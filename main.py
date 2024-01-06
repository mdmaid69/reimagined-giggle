def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"