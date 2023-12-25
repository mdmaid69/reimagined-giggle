import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h