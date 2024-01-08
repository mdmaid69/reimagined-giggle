import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())