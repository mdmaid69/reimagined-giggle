from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())