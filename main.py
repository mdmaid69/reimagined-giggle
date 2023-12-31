import logging
def setup_logging(level):
        logging.basicConfig(level=level)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"