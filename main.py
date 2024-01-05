  import os
  def get_base_name(path):
        return os.path.basename(path)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())