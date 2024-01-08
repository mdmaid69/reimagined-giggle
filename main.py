text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())