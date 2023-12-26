  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())