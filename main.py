import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)