import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)