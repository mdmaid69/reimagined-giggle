n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"