import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())