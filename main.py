import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"