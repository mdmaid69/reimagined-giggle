from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])