from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import numpy as np
print(np.array([1, 2, 3]))