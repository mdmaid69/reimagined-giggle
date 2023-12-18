import re
def split_string(pattern, string):
        return re.split(pattern, string)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())