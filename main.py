  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))