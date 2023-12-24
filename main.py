import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)