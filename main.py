  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))