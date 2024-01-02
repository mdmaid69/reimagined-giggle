  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())