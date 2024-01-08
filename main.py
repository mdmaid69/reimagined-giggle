  def remove_duplicates(lst):
        return list(set(lst))
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())