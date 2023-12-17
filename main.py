import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)