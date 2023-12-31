  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"