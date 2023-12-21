import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())