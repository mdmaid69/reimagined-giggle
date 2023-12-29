import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())