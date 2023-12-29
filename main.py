import json
def convert_to_json(data):
        return json.dumps(data)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())