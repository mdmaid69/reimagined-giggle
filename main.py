from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
import array
def get_list_from_array(array):
        return array.tolist()