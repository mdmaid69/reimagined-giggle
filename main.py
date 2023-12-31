def is_palindrome(s):
        return s == s[::-1]
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())