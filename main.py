import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))