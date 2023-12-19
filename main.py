text = "Hello, world!"
print("Uppercase:", text.upper())
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"