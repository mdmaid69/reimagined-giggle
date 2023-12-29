import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))