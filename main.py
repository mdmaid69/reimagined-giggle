import math
def calculate_arc_sine(x):
        return math.asin(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())