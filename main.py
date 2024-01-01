import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import array
def get_array_buffer_info(array):
        return array.buffer_info()