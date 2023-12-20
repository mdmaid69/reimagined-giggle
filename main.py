import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)