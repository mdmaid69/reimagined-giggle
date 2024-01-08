from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"
  import sqlite3
  def close_database_connection(connection):
        connection.close()