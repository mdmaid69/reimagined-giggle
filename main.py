import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))