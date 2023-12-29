  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())