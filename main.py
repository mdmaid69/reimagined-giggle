import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)