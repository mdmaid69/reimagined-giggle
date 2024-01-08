import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable