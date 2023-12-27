x = 10
y = 20
print("Sum:", x + y)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"