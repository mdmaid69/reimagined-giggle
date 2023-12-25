import array
def get_list_from_array(array):
        return array.tolist()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())