import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)