  def cube_number(x):
        return x**3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"