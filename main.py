import math
def calculate_error_function(x):
        return math.erf(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())