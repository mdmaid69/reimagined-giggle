import array
def check_if_array_contains_item(array, item):
        return item in array
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())