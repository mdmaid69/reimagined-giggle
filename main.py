import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())