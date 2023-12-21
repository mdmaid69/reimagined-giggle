import array
def get_array_item(array, i):
        return array[i]
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())