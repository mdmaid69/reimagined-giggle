import itertools
print(list(itertools.permutations([1, 2, 3])))
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())