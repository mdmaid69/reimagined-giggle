from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import shutil
def move_file(src, dst):
        shutil.move(src, dst)