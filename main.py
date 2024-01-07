import array
def get_array_as_bytearray(array):
        return bytearray(array)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())