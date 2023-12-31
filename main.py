import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())