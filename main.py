import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)