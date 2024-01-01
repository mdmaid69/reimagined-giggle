  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)