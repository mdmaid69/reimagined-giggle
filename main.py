from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
n = 10
print("Powers of 2:", [2**x for x in range(n)])