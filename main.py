text = "Hello, world!"
print("Characters:", len(text))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"