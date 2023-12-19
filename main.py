from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)