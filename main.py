import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()