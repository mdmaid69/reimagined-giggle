def count_words(sentence):
        return len(sentence.split())
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"