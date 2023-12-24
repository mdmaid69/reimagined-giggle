import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)