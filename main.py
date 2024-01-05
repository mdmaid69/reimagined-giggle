import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))