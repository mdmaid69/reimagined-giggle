import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"