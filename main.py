import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))