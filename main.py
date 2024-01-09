from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))