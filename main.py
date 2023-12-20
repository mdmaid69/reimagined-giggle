  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"