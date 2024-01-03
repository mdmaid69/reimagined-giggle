import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import array
def append_to_array(array, item):
        array.append(item)