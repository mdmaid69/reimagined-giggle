sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"