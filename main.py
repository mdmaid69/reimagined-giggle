import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)