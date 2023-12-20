n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"