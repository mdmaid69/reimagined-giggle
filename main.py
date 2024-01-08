import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)