import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)