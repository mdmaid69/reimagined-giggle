import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())