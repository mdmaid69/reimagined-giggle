from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))