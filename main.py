n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"