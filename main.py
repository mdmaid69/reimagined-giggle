import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))