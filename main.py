import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height