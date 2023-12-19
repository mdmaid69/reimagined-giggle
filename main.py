import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"