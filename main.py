  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h