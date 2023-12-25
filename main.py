import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)