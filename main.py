from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import platform
def get_python_version():
        return platform.python_version()