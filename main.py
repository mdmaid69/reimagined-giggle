import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)