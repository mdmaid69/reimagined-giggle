import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)