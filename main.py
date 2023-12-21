from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)