import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def get_current_working_directory():
        return os.getcwd()