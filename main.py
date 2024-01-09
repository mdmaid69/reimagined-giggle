from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
text = "Hello, world!"
print("Words:", len(text.split()))