numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"