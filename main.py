  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)