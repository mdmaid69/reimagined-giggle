def count_characters(sentence):
        return len(sentence)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"