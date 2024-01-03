import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())