from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)