from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import os
def get_environment_variable(var):
        return os.getenv(var)