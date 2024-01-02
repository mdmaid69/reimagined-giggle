  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())