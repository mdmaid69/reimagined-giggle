import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"