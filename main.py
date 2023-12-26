import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())