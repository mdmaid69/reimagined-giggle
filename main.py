import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())