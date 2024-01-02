import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())