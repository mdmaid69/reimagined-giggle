import os
print(os.getcwd())
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"