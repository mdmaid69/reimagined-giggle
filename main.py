import array
def get_string_from_array(array):
        return array.tobytes()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())