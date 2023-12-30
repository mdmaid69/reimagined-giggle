  def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())