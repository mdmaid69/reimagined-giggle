import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import array
def insert_into_array(array, i, item):
        array.insert(i, item)