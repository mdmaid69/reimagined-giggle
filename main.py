import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())