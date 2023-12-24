def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())