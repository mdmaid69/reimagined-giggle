import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)