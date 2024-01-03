  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))