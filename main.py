import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)