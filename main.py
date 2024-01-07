from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def greet(name):
        print(f"Hello, {name}!")