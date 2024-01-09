from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)