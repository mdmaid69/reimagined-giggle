import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)