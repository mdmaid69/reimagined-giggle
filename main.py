import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import os
def change_working_directory(path):
        os.chdir(path)