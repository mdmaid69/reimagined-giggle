import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"