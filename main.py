i = 0
while i < 5:
        print(i)
        i += 1
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"