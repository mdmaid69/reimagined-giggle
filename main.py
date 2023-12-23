import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()