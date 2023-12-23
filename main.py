def remove_duplicates(lst):
        return list(set(lst))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"