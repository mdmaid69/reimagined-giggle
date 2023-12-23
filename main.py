import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)