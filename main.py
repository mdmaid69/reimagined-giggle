import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]