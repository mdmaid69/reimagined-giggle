import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())