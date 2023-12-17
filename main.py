from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
def find_union(list1, list2):
        return set(list1) | set(list2)