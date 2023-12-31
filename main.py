import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())