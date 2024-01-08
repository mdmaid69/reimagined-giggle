import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import array
def iterate_over_array(array):
        for item in array:
        print(item)