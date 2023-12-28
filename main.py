import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)