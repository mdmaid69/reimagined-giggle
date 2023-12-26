import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)