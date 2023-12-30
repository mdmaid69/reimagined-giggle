import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import sqlite3
  def close_database_connection(connection):
        connection.close()