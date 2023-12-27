import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)