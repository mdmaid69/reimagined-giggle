import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())