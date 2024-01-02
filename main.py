import re
def split_string(pattern, string):
        return re.split(pattern, string)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))