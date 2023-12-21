from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import datetime
def get_current_datetime():
        return datetime.datetime.now()