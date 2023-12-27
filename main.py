from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import re
print(re.match("h.*o", "hello world"))