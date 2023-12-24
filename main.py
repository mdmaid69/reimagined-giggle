import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())