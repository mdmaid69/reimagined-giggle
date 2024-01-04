import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))