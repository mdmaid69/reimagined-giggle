  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)