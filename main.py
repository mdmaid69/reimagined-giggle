import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"