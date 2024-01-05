i = 0
while i < 5:
        print(i)
        i += 1
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())