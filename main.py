from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h