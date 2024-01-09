import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}