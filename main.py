  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))