import sys
def add_to_python_path(path):
        sys.path.append(path)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())