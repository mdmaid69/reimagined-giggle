import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value