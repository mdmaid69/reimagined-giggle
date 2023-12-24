n = 10
print("Square numbers:", [x**2 for x in range(n)])
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())