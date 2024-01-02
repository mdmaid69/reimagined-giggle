import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())