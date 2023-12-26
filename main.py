import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)