import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())