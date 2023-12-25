import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))