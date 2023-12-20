import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)