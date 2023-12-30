import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)