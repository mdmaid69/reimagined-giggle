import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))