import array
def get_array_as_int(array):
        return int(array[0])
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())