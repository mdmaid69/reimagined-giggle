import time
def get_current_time():
        return time.time()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"