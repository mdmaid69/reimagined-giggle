from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)