  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))