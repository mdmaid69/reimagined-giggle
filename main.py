import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid