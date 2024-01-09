import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)