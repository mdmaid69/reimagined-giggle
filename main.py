def sort_list(lst):
        return sorted(lst)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"