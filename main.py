import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))