import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())