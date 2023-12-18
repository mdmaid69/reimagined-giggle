numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"