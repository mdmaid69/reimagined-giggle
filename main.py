import itertools
print(list(itertools.permutations([1, 2, 3])))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"