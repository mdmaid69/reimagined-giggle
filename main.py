import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())