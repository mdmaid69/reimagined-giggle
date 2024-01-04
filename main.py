import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"