import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())