import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)