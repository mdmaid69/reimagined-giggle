import math
def calculate_square_root(x):
        return math.sqrt(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())