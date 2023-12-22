import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import datetime
print(datetime.datetime.now())