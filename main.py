import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}