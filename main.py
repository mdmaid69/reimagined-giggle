import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())