import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))