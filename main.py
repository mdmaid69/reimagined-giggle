import time
def get_current_time():
        return time.ctime()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())