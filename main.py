import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"