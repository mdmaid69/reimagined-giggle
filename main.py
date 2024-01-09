import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks