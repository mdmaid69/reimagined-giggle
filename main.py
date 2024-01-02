import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))