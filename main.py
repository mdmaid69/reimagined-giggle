import array
def convert_array_to_bytes(array):
        return array.tobytes()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())