import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
n = 10
print("Cube numbers:", [x**3 for x in range(n)])