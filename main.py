import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)