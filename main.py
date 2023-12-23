from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import random
def generate_random_sample(population, k):
        return random.sample(population, k)