import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())