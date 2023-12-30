import array
def extend_array(array, iterable):
        array.extend(iterable)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())