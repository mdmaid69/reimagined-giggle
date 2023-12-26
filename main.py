sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"