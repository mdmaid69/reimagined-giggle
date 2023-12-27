  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())