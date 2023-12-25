import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import array
def get_array_buffer_info(array):
        return array.buffer_info()