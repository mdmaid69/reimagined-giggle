n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"