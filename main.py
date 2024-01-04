import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)