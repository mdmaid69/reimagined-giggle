  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())