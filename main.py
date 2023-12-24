from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import time
def get_time_since_epoch():
        return time.time()