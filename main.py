import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import datetime
def get_today_date():
        return datetime.date.today()