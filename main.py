import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)