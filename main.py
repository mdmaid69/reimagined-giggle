import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())