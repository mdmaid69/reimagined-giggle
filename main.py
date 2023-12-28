import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())