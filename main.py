numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())