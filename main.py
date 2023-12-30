import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)