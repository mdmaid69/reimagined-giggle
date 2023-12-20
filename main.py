  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))