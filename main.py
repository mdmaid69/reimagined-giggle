def find_unique_words(sentence):
        return set(sentence.split())
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"