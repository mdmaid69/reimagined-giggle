import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)