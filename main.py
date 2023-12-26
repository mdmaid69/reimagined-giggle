import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"