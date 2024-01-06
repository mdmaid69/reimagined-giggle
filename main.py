  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())