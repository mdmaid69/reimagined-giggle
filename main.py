import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())