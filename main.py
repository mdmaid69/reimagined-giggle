  def convert_to_hex(n):
        return hex(n)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"