n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())