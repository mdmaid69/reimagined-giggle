import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))