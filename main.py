import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)