import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import datetime
  def get_current_date():
        return datetime.datetime.now().date()