import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)