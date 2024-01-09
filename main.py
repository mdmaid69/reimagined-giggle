print(sum(range(10)))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"