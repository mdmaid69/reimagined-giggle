import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
import sklearn.datasets
print(sklearn.datasets.load_iris())