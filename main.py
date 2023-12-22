import array
def get_array_as_memoryview(array):
        return memoryview(array)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))