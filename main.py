  import os
  def get_current_directory():
        return os.getcwd()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())