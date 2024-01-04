import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)