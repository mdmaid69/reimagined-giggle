  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"