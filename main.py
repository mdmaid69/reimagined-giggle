from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import shutil
def delete_directory(path):
        shutil.rmtree(path)