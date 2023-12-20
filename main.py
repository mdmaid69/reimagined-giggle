  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())