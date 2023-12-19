import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)