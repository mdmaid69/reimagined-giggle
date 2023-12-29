import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())