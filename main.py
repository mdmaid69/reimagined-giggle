import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())