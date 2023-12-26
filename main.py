from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"