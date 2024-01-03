import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())