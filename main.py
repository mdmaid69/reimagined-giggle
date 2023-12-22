import time
def get_current_time():
        return time.ctime()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"