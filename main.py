import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)