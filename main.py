import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)