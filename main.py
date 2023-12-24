import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"