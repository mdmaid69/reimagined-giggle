import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())