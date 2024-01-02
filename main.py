import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)