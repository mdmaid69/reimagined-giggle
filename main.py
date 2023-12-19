import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)