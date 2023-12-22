import time
def get_time_since_epoch():
        return time.time()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())