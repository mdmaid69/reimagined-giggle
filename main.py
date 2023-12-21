import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)