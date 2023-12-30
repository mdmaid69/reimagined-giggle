  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())