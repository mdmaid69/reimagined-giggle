import array
def remove_from_array(array, item):
        array.remove(item)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())