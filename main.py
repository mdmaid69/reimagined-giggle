n = 10
print("Powers of 2:", [2**x for x in range(n)])
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())