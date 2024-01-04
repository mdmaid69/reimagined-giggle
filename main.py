import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())