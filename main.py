from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"