import json
print(json.dumps({"name": "John", "age": 30}))
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"