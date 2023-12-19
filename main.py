n = 10
print("Square numbers:", [x**2 for x in range(n)])
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"