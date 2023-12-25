import datetime
def get_current_datetime():
        return datetime.datetime.now()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())