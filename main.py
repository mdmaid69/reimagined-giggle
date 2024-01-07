import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())