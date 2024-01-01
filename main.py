import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)