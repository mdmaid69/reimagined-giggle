import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)