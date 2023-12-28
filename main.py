import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)