from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])