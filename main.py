import array
def get_array_typecode(array):
        return array.typecode
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())