  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())