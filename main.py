import math
def calculate_cosine(x):
        return math.cos(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())