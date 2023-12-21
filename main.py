import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())