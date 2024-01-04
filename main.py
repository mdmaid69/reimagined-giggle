import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)