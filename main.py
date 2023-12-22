import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)