import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)