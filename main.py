import platform
def get_python_version():
        return platform.python_version()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())