from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))