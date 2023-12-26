import math
def calculate_sign(x):
        return math.copysign(1, x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())