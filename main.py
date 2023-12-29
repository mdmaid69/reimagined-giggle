import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)