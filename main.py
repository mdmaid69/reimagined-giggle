import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())