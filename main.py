  def calculate_area_triangle(b, h):
        return 0.5 * b * h
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())