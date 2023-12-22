import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())