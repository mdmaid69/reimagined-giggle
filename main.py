import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)