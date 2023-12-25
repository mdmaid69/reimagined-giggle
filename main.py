from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import random
def roll_die():
        return random.randint(1, 6)