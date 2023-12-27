  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())