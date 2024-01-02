  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())