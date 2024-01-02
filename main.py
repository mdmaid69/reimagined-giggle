import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())