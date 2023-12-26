import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"