import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import collections
def count_elements(iterable):
        return collections.Counter(iterable)