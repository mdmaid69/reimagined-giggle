for i in range(5):
        print(i)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"