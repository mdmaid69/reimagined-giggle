  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())