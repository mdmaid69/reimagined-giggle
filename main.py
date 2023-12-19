import math
def calculate_exponential(x):
        return math.exp(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())