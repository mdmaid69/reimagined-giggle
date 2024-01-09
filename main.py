import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())