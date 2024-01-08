from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")