  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"