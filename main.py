import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))