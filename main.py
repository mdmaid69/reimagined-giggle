x = 10
y = 20
print("Sum:", x + y)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())