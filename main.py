import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"