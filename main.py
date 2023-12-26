import random
print(random.randint(0, 100))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"