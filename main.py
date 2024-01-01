from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
n = 10
print("Cube numbers:", [x**3 for x in range(n)])