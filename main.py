  import sqlite3
  def close_database_connection(connection):
        connection.close()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))