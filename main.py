  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"