  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)