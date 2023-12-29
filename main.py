import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)