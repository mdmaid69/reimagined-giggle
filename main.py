from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()