from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])