import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())