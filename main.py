import os
def list_files_in_directory(path):
        return os.listdir(path)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())