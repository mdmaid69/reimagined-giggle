import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"