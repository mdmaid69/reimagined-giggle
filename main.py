  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())