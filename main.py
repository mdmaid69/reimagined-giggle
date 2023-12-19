import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())