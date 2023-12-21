import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())