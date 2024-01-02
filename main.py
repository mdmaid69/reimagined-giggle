import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"