import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import collections
def create_ordered_dict():
        return collections.OrderedDict()