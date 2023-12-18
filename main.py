import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))