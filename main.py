import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))