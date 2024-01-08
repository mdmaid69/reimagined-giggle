  import os
  def delete_file(file_name):
        os.remove(file_name)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())