import random
def generate_random_choice(choices):
        return random.choice(choices)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"