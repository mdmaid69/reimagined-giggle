  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread