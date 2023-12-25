import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))