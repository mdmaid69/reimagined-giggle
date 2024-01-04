import math
def calculate_absolute_value(x):
        return math.fabs(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())