import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))