import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)