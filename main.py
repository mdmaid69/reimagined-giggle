import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import json
def read_from_json(json_string):
        return json.loads(json_string)