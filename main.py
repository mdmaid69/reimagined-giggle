import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])