  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())