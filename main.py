  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))