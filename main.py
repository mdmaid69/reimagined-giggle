import array
def convert_array_to_list(array):
        return array.tolist()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())