import json
print(json.dumps({"name": "John", "age": 30}))
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())