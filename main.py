import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())